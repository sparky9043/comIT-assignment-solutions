class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name
        self.description = description
        self.base_price = base_price
        
    def __str__(self):
        return f"{self.name=} {self.description=} {self.base_price=}"
    