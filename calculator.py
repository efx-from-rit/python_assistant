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


def main():
    # print(addition())
    print(subtraction())

if __name__ == "__main__":
    main()
