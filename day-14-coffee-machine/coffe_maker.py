MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25
}

user_money = 0
is_machine_in_work = True
is_first_action = True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${user_money}")


def get_coffee(type):
    global user_money

    price = MENU[type]["cost"]
    water = MENU[type]["ingredients"]["water"]
    milk = 0
    if type != 'espresso':
        milk = MENU[type]["ingredients"]["milk"]

    coffe = MENU[type]["ingredients"]["coffee"]

    if is_user_has_enough_money(price) and is_machine_has_enough_resources(water, milk, coffe):
        prepare_coffe(price, coffe, milk, water)
        print(f"Here is your {type}. Enjoy!")
        return_change()
    elif not is_user_has_enough_money(price):
        print('No enough money')
        return_change()
    elif not is_machine_has_enough_resources(water, milk, coffe):
        print(f"Sorry there no enough {' and '.join(what_resources_not_enough(water, milk, coffe))}")
        return_change()


def espresso():
    get_coffee("espresso")


def latte():
    get_coffee("latte")


def cappuccino():
    get_coffee("cappuccino")


def what_resources_not_enough(water, milk, coffe):
    resource = []
    if resources["water"] - water < 0:
        resource.append("water")
    if resources["milk"] - milk < 0:
        resource.append("milk")
    if resources["coffee"] - coffe < 0:
        resource.append("coffee")

    return resource


def return_change():
    global user_money
    print(f'Here is ${user_money} in change.')
    user_money = 0


def prepare_coffe(price, coffe, milk, water):
    global user_money
    user_money -= price
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffe


def is_user_has_enough_money(price):
    return user_money - price >= 0


def is_machine_has_enough_resources(water, milk, coffe):
    return resources["water"] - water >= 0 and resources["milk"] - milk >= 0 and resources["coffee"] - coffe >= 0


actions = {
    'report': report,
    'espresso': espresso,
    'latte': latte,
    'cappuccino': cappuccino
}


def ask_user_action():
    return input('What would you like? (espresso/latte/cappuccino): ').lower()


def insert_money():
    global user_money
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    user_money = round(
        coins['quarter'] * quarters + coins['dime'] * dimes + coins['nickel'] * nickles + coins['penny'] * pennies, 2)


def use_machine():
    global is_machine_in_work
    if input("Would you like a use coffee-machine 'Y' or 'N': ").lower() == 'n':
        is_machine_in_work = False


use_machine()

while is_machine_in_work:
    action_now = ask_user_action()
    if action_now == 'report':
        action_now_func = actions[action_now]
        action_now_func()
    else:
        action_now_func = actions[action_now]
        insert_money()
        action_now_func()
    use_machine()