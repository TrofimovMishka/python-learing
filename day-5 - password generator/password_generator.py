import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword generator\n")
count_letters = int(input('How many letters would you like?\n'))
count_symbols = int(input('How many symbols would you like?\n'))
count_numbers = int(input('How many numbers would you like?\n'))

password_list = []

for i in range(count_letters):
    password_list.append(letters[random.randint(1, len(letters)-1)])
    # random.choice(letters) -> this return pseudo random letter from list

for i in range(count_symbols):
    password_list.append(symbols[random.randint(1, len(symbols)-1)])
    # random.choice(symbols) -> this return pseudo random letter from list

for i in range(count_numbers):
    password_list.append(numbers[random.randint(1, len(numbers)-1)])
    # random.choice(numbers) -> this return pseudo random letter from list

password = ''

random.shuffle(password_list)

for i in password_list:
    password += i

print(password)
