def fahrenheit_converter(celsius):
    return ((9/5)*(celsius)) + 32

def celsius_converter(fahrenheit):
    return ((5/9)*(fahrenheit - 32))

def feet_converter(meters):
    return meters * 3.28084

def meters_converter(feet):
    return feet / 3.28084

def unit_converter():
    while True:
        print("========== UNIT CONVERTER ==========")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Meters to Feet")
        print("4. Feet to Meters")
        print("5. Return to main menu")
        print("====================================")
        choice = input("Enter your choice: ")
        if choice == "1":
            celsius = input("Enter degrees celsius: ")
            try:
                celsius = float(celsius)
                result = fahrenheit_converter(celsius)
                print(result, "degrees fahrenheit\n")
            except ValueError:
                print("Invalid entry. Must be a numeric value\n")
        elif choice == "2":
            fahrenheit = input("Enter degrees fahrenheit: ")
            try:
                fahrenheit = float(fahrenheit)
                result = celsius_converter(fahrenheit)
                print(result, "degrees celsius\n")
            except ValueError:
                print("Invalid entry. Must be a numeric value\n")
        elif choice == "3":
            meters = input("Enter meters: ")
            try:
                meters = float(meters)
                result = feet_converter(meters)
                print(result, "feet\n")
            except ValueError:
                print("Invalid entry. Must be a numeric value\n")
        elif choice == "4":
            feet = input("Enter feet: ")
            try:
                feet = float(feet)
                result = meters_converter(feet)
                print(result, "meters\n")
            except ValueError:
                print("Invalid entry. Must be a numeric value\n")
        elif choice == "5":
            print("Returning to main menu...\n")
            break
        else:
            print("Invalid selection. Try again.\n")

if __name__ == "__main__":
    unit_converter()