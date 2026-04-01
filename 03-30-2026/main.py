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
    print_center("2. Add a car")
    print_divider()

    choice = int(input("Enter your selection (1-6): "))
    return choice

def main():
    # initialize_database()
    # import_cars()
    choice = show_menu()

    cars = get_all_cars()
    for car in cars:
        print(car)

main()