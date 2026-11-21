""" IMPORTS """
import random

def is_reversed_range(a, b):
    return a > b

def generate_number(a, b):
    if is_reversed_range(a, b):
        return None
    return random.randint(a, b)

def get_range():
    while True:
        try:
            minimum = int(input("Enter minimum value: "))
            maximum = int(input("Enter maximum value: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            if is_reversed_range(minimum, maximum):
                print("Minimum is larger than maximum. Please re-enter your values.")
            else:
                break
    return minimum, maximum

def random_menu():
    while True:
        print("========== RANDOM NUMBER GENERATOR ==========")
        print("1. Generate Random Number")
        print("2. Exit")
        print("=============================================")
        choice = input("Enter your choice: ")

        if choice == "1":
            num_range = get_range()
            minimum = num_range[0]
            maximum = num_range[1]
            result = generate_number(minimum, maximum)
            print("Random Number:", result, "\n")
        elif choice == "2":
            print("Returning to main menu...\n")
            break
        else:
            print("Invalid selection. Try again.\n")

if __name__ == "__main__":
    random_menu()