# addition function:
def addition():
    sum_of_numbers = 0 # sum of numbers starts at zero
    while True: # infinite loop; user keeps entering values until they choose to exit
        try:
            number = input('Enter a number (press "E" to leave): ')
            if number == "E" or number == "e":
                break # leaves function if user types "e" or "E"
            else:
                sum_of_numbers += float(number) # adds entered number to last sum value
                print("Sum =", sum_of_numbers) # shows the user the current sum
        except ValueError: # printed if user enters non-numeric value
            print("Non-numeric value entered.")

    return sum_of_numbers # returns the sum to be accessed by other functions

# subtraction function:
def subtraction():
    difference = input("Enter starting number: ") # enters a starting number for the user to subtract from
    while True:
        try:
            difference = float(difference)
            number = input('Enter a number (press "E" to leave): ') # user enters number to be subtracted from starting number (subtrahend)
            if number == "E" or number == "e": # checks if user tried to leave function
                break # leaves function
            else:
                difference -= float(number) # subtracts entered value from starting number
                print("Difference =", difference)
        except ValueError:
            print("Non-numerical value entered.")

    return difference # returns difference to be accessed by other functions

# multiplication function:
def multiplication():
    starting_number = float(input("Enter your starting number: ")) # enters a starting number for the user to multiply from
    while True: # initiates infinite loop; same case as subtraction function
        try:
            number = input('Enter a number (press "E" to leave): ') # user enters number to be multipled with the starting number (multiplier)
            if number == "E" or number == "e": # checks if user tried to leave function
                break # leaves function
            else:
                starting_number *= float(number) # multiplies the multiplicand (starting number) by the multiplier
                print("Product =", starting_number) # displays the current product in terminal
        except ValueError: # printed if user enters non-numeric value
            print("Non-numeric value entered.")

    return starting_number # returns product (ignore variable name) to be accessed by other functions

# division function:
def division():
    quotient = 0 # quotient starts at zero
    while True: # initiates infinite loop; same case as multiplication function
        numerator = input("Enter numerator: ") # prompts user to enter numerator
        denominator = input("Enter denominator: ") # prompts user to enter denominator
        
        if numerator == "E" or numerator == "e" or denominator == "E" or denominator == "e": # checks if user tried to leave function
            break # leaves function
        try:
            quotient = float(numerator) / float(denominator) # calculates quotient
            print("Quotient =", quotient) # prints quotient to terminal
        except ZeroDivisionError: # printed if user tries to divide by zero
            print("Cannot divide by zero.")
        except ValueError: # printed if user enters non-numeric value
            print("Non-numeric value entered.")

    return quotient # returns quotient to be accessed by other functions

def main():
    # these were all tests
    # print(addition())
    print(subtraction())
    # print(multiplication())
    # print(division())

if __name__ == "__main__":
    main()
