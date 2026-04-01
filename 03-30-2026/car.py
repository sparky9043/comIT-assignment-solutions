class Car:
    def __init__(self, make: str, model: str, year: int,
                 price: float, mileage: int, id = None):
        # Your code here
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.id = id

    def __str__(self):
        return (f"[ID: {self.id}] {self.year} {self.make + self.model} | "
            f"${self.price:,.2f} | {self.mileage:,} km")

# car = Car('Toyota', 'Camry', 2021, 24999.99, 15000, id=1)
# print(car)