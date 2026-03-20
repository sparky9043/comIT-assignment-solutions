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
        
cafe = Cafe("Sunny Bean Café", tax_rate=0.08)

# Create Coffee objects and add them to the menu
cafe.add_to_menu(Coffee("Espresso",    "Strong and bold shot of coffee",           2.50))
cafe.add_to_menu(Coffee("Americano",   "Espresso diluted with hot water",          3.00))
cafe.add_to_menu(Coffee("Cappuccino",  "Equal parts espresso, foam, and milk",     3.75))
cafe.add_to_menu(Coffee("Latte",       "Creamy espresso with lots of steamed milk",3.50))
cafe.add_to_menu(Coffee("Flat White",  "Velvety milk with a double espresso shot", 4.00))
cafe.add_to_menu(Coffee("Macchiato",   "Espresso 'stained' with a touch of foam",  3.25))
cafe.add_to_menu(Coffee("Mocha",       "Espresso with chocolate and steamed milk", 4.25))
cafe.add_to_menu(Coffee("Cold Brew",   "Slow-steeped coffee served cold",          4.00))

SIZES = ["small", "medium", "large"]

print(f"\nWelcome to {cafe.name}! ☕")

while True:
    print("\n" + "="*40)
    print("What would you like to do?")
    print("1. View menu and order a drink")
    print("2. View current order")
    print("3. Checkout and pay")
    print("="*40)

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        # Show menu
        cafe.display_menu()

        # Ask the customer to pick a drink (validate input!)
        drink_input = input("\nEnter the number of the drink you want (or 0 to cancel): ").strip()

        if drink_input == "0":
            continue   # go back to the top of the while loop

        # Check that the input is a valid number
        if not drink_input.isdigit():
            print("❌ Please enter a number.")
            continue

        drink_index = int(drink_input) - 1   # subtract 1 because lists start at 0

        if drink_index < 0 or drink_index >= len(cafe.menu):
            print("❌ That number is not on the menu. Try again.")
            continue

        selected_coffee = cafe.menu[drink_index]

        # Show sizes
        cafe.display_sizes()
        size_input = input("Enter the number of the size you want: ").strip()

        if not size_input.isdigit():
            print("❌ Please enter a number.")
            continue

        size_index = int(size_input) - 1

        if size_index < 0 or size_index >= len(SIZES):
            print("❌ Invalid size. Try again.")
            continue

        selected_size = SIZES[size_index]

        # Add the order
        cafe.add_order(selected_coffee, selected_size)

    elif choice == "2":
        if not cafe.orders:
            print("\n🛒 Your order is empty.")
        else:
            print("\n--- Your Current Order ---")
            for i, order in enumerate(cafe.orders, start=1):
                print(f"  {i}. {order}")
            print(f"  Subtotal so far: ${cafe.calculate_subtotal():.2f}")

    elif choice == "3":
        if not cafe.orders:
            print("\n❌ You have not ordered anything yet!")
            continue

        # Ask for tip percentage
        print("\nHow much would you like to tip?")
        print("1. 10%    2. 15%    3. 20%    4. No tip")
        tip_choice = input("Enter your choice (1/2/3/4): ").strip()

        tip_map = {"1": 10, "2": 15, "3": 20, "4": 0}
        tip_percent = tip_map.get(tip_choice, 0)

        cafe.print_bill(tip_percent)
        print("\nThank you for visiting! Have a great day! ☕\n")
        break   # Exit the while loop — we are done!

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")