class Car:
    """Represents a Car and its various properties

    Attributes:
        make (str): The make of the car
        model (str): The model of the car
        year (int): The manufacture year of the car
        price (float): The unit price of the car
        mileage (int): The mileage of the car
        id (int): unique integer identifier for the car
    """
    def __init__(self, make: str, model: str, year: int,
                 price: float, mileage: int, id = None):
        """Initializes the car object with arguments

        Args:
            make (str): The make of the car
            model (str): The model of the car
            year (int): The manufacture year of the car; must be at least 0
            price (float): The unit price of the car; must be at least 0
            mileage (int): The mileage of the car; must be at least 0
            id (int): unique integer identifier for the car; None by default
        """
        if year < 0 or price < 0 or mileage < 0:
            raise ValueError('year, price and mileage must be at least 0')

        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.id = id

    def __str__(self):
        return (f"[ID: {self.id}] {self.year} {self.make + " " + self.model} | "
            f"${self.price:,.2f} | {self.mileage:,} km")
    
    def to_tuple(self):
        """Converts the car object's make, model, year, price and mileage
        to tuples

        Returns:
            tuple: An order tuple of the car's basic information
        """
        return (self.make, self.model, self.year, self.price, self.mileage)

# car = Car('Toyota', 'Camry', 2021, 24999.99, 15000, id=1)
# print(car.to_tuple())
# print(car)