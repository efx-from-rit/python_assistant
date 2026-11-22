""" IMPORTS """
import sys
import calculator
import random_generator
import unit_converter

def welcome_message():
    # method variables:
    option1 = "1. Calculator"
    option2 = "2. Random Number Generator"
    option3 = "3. Text Analyzer"
    option4 = "4. Password Generator"
    option5 = "5. To-Do List"
    option6 = "6. Unit Converter"
    option7 = "7. Quit"
    not_available = "Feature not available yet, come back soon!"

    # infinite while loop so the user can keep using the program until they decide to quit
    while True:
        # Python Assistant Header:
        print("==========================================================")
        print("                    PYTHON ASSISTANT")
        print("==========================================================\n")

        # Welcome Message:
        print("Hello, I am your python assistant! What would you like to do?")

        print(option1, "\n", option2, "\n", option3, "\n", option4, "\n", option5, "\n", option6, "\n", option7, "\n")

        user_choice = input("Enter your choice here (by number): ")

        if user_choice == "1":
            calculator.calc_menu()
        elif user_choice == "2":
            random_generator.random_menu()
        elif user_choice == "3":
            print(not_available)
        elif user_choice == "4":
            print(not_available)
        elif user_choice == "5":
            print(not_available)
        elif user_choice == "6":
            unit_converter.unit_converter()
        elif user_choice == "7": # 7 = "Quit" option
            answer = input("Are you sure you want to quit the program (y/n)? ") # double checks with the user for confirmation
            if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
                sys.exit() # exits the program
        else:
            print("Not one of the presented options") # good for if the user misclicks or mistypes something

def main():
    welcome_message()

if __name__ == "__main__": # run-guard for later testing
    main()