# Step 1
class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name
        self.description = description
        self.base_price = base_price
        
    def __str__(self):
        return f"{self.name} {self.description} {self.base_price}".title()

# Step 2 
class Order:
    def __init__(self, coffee: Coffee, size: str):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()
    
    def calculate_price(self):
        final_price = self.coffee.base_price
        
        if self.size == 'medium':
            final_price += 0.50
        elif self.size == 'large':
            final_price += 1
        
        return final_price

    def  __str__(self):
        return f"{self.size} {self.coffee.name} ${self.price}".title()
    
coffee = Coffee('Latte', 'a delicious coffee with milk', 4.00)

order = Order(coffee, 'medium')

# Step 3