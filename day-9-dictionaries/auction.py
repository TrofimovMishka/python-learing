import os

import art

dictionary = {}
is_end = False


def clear():
    os.system('clear')


print(art.logo)


def ask_name():
    return input("What's your name? ")


def ask_bid_prive():
    return int(input("What's your bid? $"))


def is_there_others():
    return input("Is there are others who want to bid? ")


def get_winner():
    price = 0
    winner = ''

    for name in dictionary:
        if dictionary[name] > price:
            price = dictionary[name]
            winner = name

    print(f"The winner is {winner} with a bid of ${price}")


while not is_end:
    name = ask_name()

    dictionary[name] = ask_bid_prive()

    if is_there_others().lower() == 'yes':
        clear()
    else:
        clear()
        get_winner()
        is_end = True
