from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                        get_car_by_id, update_car, delete_car, search_cars)

def print_center(text):
    """Print user-provided text to the center of 40 characters
    
    Args:
        text (str): User-provided text to print to center
    """
    print(f"{text:^80}")

def print_divider(shape="=", number=80):
    """Print user-provided shape number of times

    Args:
        shape (str): user-defined str to print
        number (int): number of shapes to print
    """
    print(shape * number)

def wait_user_enter():
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
            wait_user_enter()
            continue

        if choice < 1 or choice > 6:
            print("ValueError:", "Please print a number between 1 to 6")
            wait_user_enter()
            continue

        if choice == 6:
            break

        if choice == 2:
            cars = get_all_cars()
            print_divider()
            print_center("List of Cars")
            if len(cars) == 0:
                print("There are no cars in the inventory")
                wait_user_enter()
                continue
            for car in cars:
                print(car)
            print_divider()
            wait_user_enter()
main()