""" FILLING NUMBERS LIST """
def get_numbers():
    numbers = []
    while True:
        value = input("Enter a number: ").strip()
        if value.lower() == 'e':
            break
        try:
            value = float(value)
            numbers.append(value)
        except ValueError:
            print("Invalid number entered.")
    return numbers

""" ADDITION """
def addition(numbers):
    total = 0 # sum of numbers starts at zero
    if len(numbers) == 0:
        return None
    for value in numbers:
        total += value
    return total

""" SUBTRACTION """
def subtraction(numbers):
    if len(numbers) == 0:
        return None
    diff = numbers[0]
    for index in range(1, len(numbers)):
        diff -= numbers[index]
    return diff

""" MULTIPLICATION """
def multiplication(numbers):
    product = 1
    if len(numbers) == 0:
        return None
    for value in numbers:
        product *= value
    return product

""" DIVISION """
def division(numbers):
    if len(numbers) == 0:
        return None
    quotient = numbers[0] # quotient starts at first index
    for index in range(1, len(numbers)):
        try:
            quotient /= numbers[index]
        except ZeroDivisionError:
            return None
    return quotient

def calc_menu():
    while True:
        """ CALCULATOR MENU """
        print("===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit\n")
        
        choice = input("Select an operation: ").strip()
        if choice == "1":
            numbers = get_numbers()
            result = addition(numbers)
            print("Sum:", result, "\n")
        elif choice == "2":
            numbers = get_numbers()
            result = subtraction(numbers)
            print("Difference:", result, "\n")
        elif choice == "3":
            numbers = get_numbers()
            result = multiplication(numbers)
            print("Product:", result, "\n")
        elif choice == "4":
            numbers = get_numbers()
            result = division(numbers)
            print("Quotient:", result, "\n")
        elif choice == "5":
            print("Exiting calculator...")
            break
        else:
            print("Invalid menu selection. Please try again.\n")

if __name__ == "__main__":
    calc_menu()
