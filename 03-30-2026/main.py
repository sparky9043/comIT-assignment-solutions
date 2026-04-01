from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                        get_car_by_id, update_car, delete_car, search_cars)

def print_center(text):
    print(f"{text:^40}")

def print_divider(shape="=", number=40):
    print(shape * number)

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
            print("Please enter a valid number")
            continue

        if choice < 1 or choice > 6:
            print("Please print a number between 1 to 6")
            continue

        if choice == 6:
            break
main()