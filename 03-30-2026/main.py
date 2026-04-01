from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                        get_car_by_id, update_car, delete_car, search_cars)

def print_center(text):
    """Print user-provided text to the center of 40 characters
    
    Args:
        text (str): User-provided text to print to center
    """
    print(f"{text:^80}")

def add_car_flow():
    try:
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = int(input("Enter car manufacture year (>0): "))
        price = float(input("Enter car price (>0.00): "))
        mileage = int(input("Enter car mileage: "))
        
        new_car = Car(make, model, year, price, mileage)
        add_car(new_car)

        print("🚗 Car added successfully!")
    except ValueError:
        print("❌ Please make sure all your values are correct")
        wait_for_user()

def view_car_flow():
    cars = get_all_cars()
    print_divider()
    print_center("List of Cars")
    if len(cars) == 0:
        print("❌ There are no cars in the inventory")
    else:
        for car in cars:
            print(car)
        print_divider()
    wait_for_user()

def update_car_flow():
    try:
        car_id = int(input("Enter car id: "))
        saved_car = get_car_by_id(car_id)

        if not saved_car:
            raise ValueError("Car Not Found")
        
        print_divider()
        print_center(f"Current: {saved_car}")
        print_divider()

        print("Enter values you want to update. Press Enter to keep current value")
        
        make = input("Enter car make: ") or saved_car.make
        model = input("Enter car model: ") or saved_car.model
        year = input("Enter car manufacture year (>0): ") or saved_car.year
        price = input("Enter car price (>0.00): ") or saved_car.price
        mileage = input("Enter car mileage: ") or saved_car.mileage
        
        updated_car = Car(make, model, int(year), float(price), int(mileage), id=car_id)
        update_car(updated_car)
        print_center('🚗 Car Updated Successfully!')
        print_center(f"Updated: {updated_car}")
        print_divider()
        wait_for_user()

    except ValueError as e:
        print_divider()
        print_center(f"Error: {e}")
        print_divider()
        wait_for_user()

def delete_car_flow():
    try:
        car_id = int(input("Enter car id: "))
        saved_car = get_car_by_id(car_id)

        if not saved_car:
            raise ValueError("Car Not Found")
        
        print_divider()
        print(saved_car)
        print_divider()

        yes_or_no = input("Are you sure? (y/n): ")

        if yes_or_no.lower() in ['y', 'yes']:
            delete_car(car_id)
            print_center("Car deleted successfully")
        elif yes_or_no.lower() in ['n', 'no']:
            print_center('Delete canceled')
        wait_for_user()

    except ValueError as e:
        print_divider()
        print_center(f"Error: {e}")
        print_divider()
        wait_for_user()

def print_divider(shape="=", number=80):
    """Print user-provided shape number of times

    Args:
        shape (str): user-defined str to print
        number (int): number of shapes to print
    """
    print(shape * number)

def wait_for_user():
    input("Press enter to continue...")

def show_menu():
    print()
    print_divider()
    print_center(" 🚗 CAR DEALERSHIP MANAGER")
    print_divider()
    # Print options 1–6 here
    # Return the user's input
    print_center("- MAIN MENU -")
    print_center("1. Add a car")
    print_center("2. View All Cars")
    print_center("3. Update Car")
    print_center("4. Delete Car")
    print_center("5. Search Cars")
    print_center("6. Exit")
    print_divider()

    choice = input("Enter your selection (1-6): ")
    return choice

def main():
    # initialize_database()
    # import_cars()
    while True:
        try: 
            choice = int(show_menu())
        except ValueError:
            print("TypeError:", "Please enter a valid number")
            wait_for_user()
            continue

        if choice < 1 or choice > 6:
            print("ValueError:", "Please print a number between 1 to 6")
            wait_for_user()
            continue

        if choice == 6:
            break

        if choice == 1:
            add_car_flow()

        elif choice == 2:
            view_car_flow()
        
        elif choice == 3:
            update_car_flow()

        elif choice == 4:
            delete_car_flow()

main()