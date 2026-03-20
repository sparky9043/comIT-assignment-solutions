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
        return f"{self.size} {self.coffee.name} ${self.price:.2f}".title()
    
latte = Coffee('Latte', 'a delicious coffee with milk', 4.00)
french_vanilla = Coffee('French Vanilla', 'coffee from france', 5.00)
hazelnut = Coffee('Hazelnut Latte', 'latte with hazelnut flavor', 4.50)

order = Order(latte, 'medium')

# Step 3
class Cafe:
    def __init__(self, name: str, tax_rate=0.08):
        self.name = name
        self.menu = []       # empty list — we will fill it with coffees
        self.orders = []     # empty list — orders are added as the customer shops
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee: Coffee):
        """Add a Coffee object to the menu list."""
        if coffee:
            self.menu.append(coffee)
            
    def display_menu(self):
        """Print the full menu with numbers so the customer can pick."""
        # Print a header with the café name
        # Loop through self.menu with enumerate() to show numbers
        # Example output:
        #   === SUNNY BEAN CAFÉ MENU ===
        #   1. Espresso       - Strong and bold shot of coffee    - $2.50
        #   2. Americano      - Espresso diluted with hot water   - $3.00
        # YOUR CODE HERE
        print(f"==== {self.name} Menu ====".upper())
        
        for index, coffee in enumerate(self.menu):
            print(f"{index + 1:<3} {coffee.name:<20} {coffee.description.title():<30} ${coffee.base_price:.2f}")
            
    def display_sizes(self):
        sizes = { "small": 0, "medium": 0.50, "large": 1 }
        
        print("==== Sizes available ===")
        for size, price in sizes.items():
            print(f"{size.title():<10} +${price:.2f}")
            
    def add_order(self, coffee, size):
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"New Order: {new_order}")
        
    def calculate_subtotal(self):
        return sum([order.calculate_price() for order in self.orders])
    
    def print_bill(self, tip_percent):
        """Print a formatted receipt with subtotal, tax, tip, and grand total."""
        subtotal = self.calculate_subtotal()
        tax = subtotal * self.tax_rate
        tip = subtotal * (tip_percent / 100)
        total = subtotal + tax + tip
        print("=" * 50)
        print(f"{self.name:^50}".upper())
        print("=" * 50)
        
        for order in self.orders:
            print(f" {order.size.title() + " " + order.coffee.name:<40} ${order.calculate_price():>5.2f}")
        
        print("-" * 50)
        
        print(f" Subtotal {"$ " + f"{subtotal:.2f}":>38}")
        print(f" Tax ({int(self.tax_rate * 100)}%) {"$ " + f"{tax:.2f}":>38}")
        print(f" Tip ({tip_percent}%) {"$ " + f"{tip:.2f}":>37}")
        
        print("=" * 50)

        print(f" TOTAL {"$ " + f"{total:.2f}":>41}")
        
my_cafe = Cafe('Starbucks Cafe')
my_cafe.add_to_menu(latte)
my_cafe.add_to_menu(french_vanilla)
my_cafe.add_to_menu(hazelnut)

my_cafe.add_order(french_vanilla, "medium")
my_cafe.add_order(french_vanilla, "large")
my_cafe.add_order(latte, "small")
my_cafe.add_order(latte, "medium")

# print(my_cafe.calculate_subtotal())
my_cafe.print_bill(15)

# my_cafe.display_menu()
# my_cafe.display_sizes()