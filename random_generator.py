import random

def generate_number(a, b):
    if a > b:
        return None
    return random.randint(a, b)

def rand_gen_menu():
    rand_num = generate_number(100, 1)
    print(rand_num)

if __name__ == "__main__":
    rand_gen_menu()