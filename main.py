import sys

def welcome_message():
    # method variables:
    option1 = "1. Calculator"
    option2 = "2. Text Analyzer"
    option3 = "3. Password Generator"
    option4 = "4. To-Do List"
    option5 = "5. Quit"
    not_available = "Feature not available yet, come back soon!"

    # Python Assistant Header:
    print("==========================================================")
    print("                    PYTHON ASSISTANT")
    print("==========================================================\n")

    # Welcome Message:
    print("Hello, I am your python assistant! What would you like to do?")

    print(option1, "\n", option2, "\n", option3, "\n", option4, "\n", option5, end = "\t")

    # infinite while loop so the user can keep using the program until they decide to quit
    while True:
        user_choice = input("\nEnter your choice here (by number): ")

        if user_choice == "1":
            print(not_available)
        elif user_choice == "2":
            print(not_available)
        elif user_choice == "3":
            print(not_available)
        elif user_choice == "4":
            print(not_available)
        elif user_choice == "5": # 5 = "Quit" option
            answer = input("Are you sure you want to quit the program (y/n)? ") # double checks with th euser for confirmation
            if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
                sys.exit() # exits the program
        else:
            print("Not one of the presented options") # good for if the user misclicks or mistypes something

def main():
    welcome_message()

if __name__ == "__main__": # run-guard for later testing
    main()