def fahrenheit_converter(celsius):
    return ((9/5)*(celsius)) + 32

def celsius_converter(fahrenheit):
    return ((5/9)*(fahrenheit - 32))

def unit_converter():
    fahrenheit = 212
    result = celsius_converter(fahrenheit)
    print(result)

if __name__ == "__main__":
    unit_converter()