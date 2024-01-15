import art

print(art.logo)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def get_first_num():
    return float(input('What the first number? '))


def get_second_num():
    return float(input('What the second number? '))


def get_operation():
    for symb in operations:
        print(symb)
    return input('What the operation? ')


def is_finish(number):
    if input(f"Type 'y' to continue calculating with {number}, or type 'n' to exit.: ").lower() == 'n':
        return True
    else:
        print('Goodbye, Bob!')
        return False


def calc():
    is_exit = False
    num1 = get_first_num()

    while not is_exit:
        operation = get_operation()
        num2 = get_second_num()
        calc_func = operations[operation]
        result = calc_func(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        num1 = result
        is_exit = is_finish(result)


# Then you can use recursion to run new calculations
calc()
