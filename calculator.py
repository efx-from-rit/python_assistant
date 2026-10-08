def addition():
    sum_of_numbers = 0
    while True:
        try:
            number = input('Enter a number (press "E" to leave): ')
            if number == "E" or number == "e":
                break
            else:
                sum_of_numbers += float(number)
                print("Current sum:", sum_of_numbers)
        except ValueError:
            print("Non-numeric value entered.")

    return sum_of_numbers

def subtraction():
    difference = float(input("Enter starting number: "))
    while True:
        try:
            number = input('Enter a number (press "E" to leave): ')
            if number == "E" or number == "e":
                break
            else:
                sum_of_numbers -= float(number)
                print("Current value:", difference)
        except ValueError:
            print("Non-numeric value entered.")

    return difference

def multiplication():
    starting_number = float(input("Enter your starting number: "))

    while True:
        try:
            number = input('Enter a number (press "E" to leave): ')
            if number == "E" or number == "e":
                break
            else:
                starting_number *= float(number)
                print("Current value:", starting_number)
        except ValueError:
            print("Non-numeric value entered.")

    return starting_number

def division():
    quotient = 0
    
    while True:
        numerator = input("Enter numerator: ")
        denominator = input("Enter denominator: ")
        
        if numerator == "E" or numerator == "e" or denominator == "E" or denominator == "e":
            break
        try:
            quotient = float(numerator) / float(denominator)
            print(quotient)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except ValueError:
            print("Non-numeric value entered.")

    return quotient

def main():
    # print(addition())
    # print(subtraction())
    # print(multiplication())
    print(division())

if __name__ == "__main__":
    main()
