import random

print("Hello day 3")

var_a = 12
var_b = 3
greetings = 'Hello bob'

if var_a > 3 and var_b < 4:
    print(greetings)
elif var_b == 3 or var_a <= 13:
    print("Bob")
else:
    print(12)

for num in range(1, 100, 5):
    print(random.randrange(3, 99393993, 43))


def is_year_leap(year):
    leap = 'Leap year'
    not_leap = 'Not leap year'

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(leap)
            else:
                print(not_leap)
        else:
            print(leap)
    else:
        print(not_leap)

is_year_leap(2016)


bill = 0

print(f'Your final bill is: ${bill}.')

name_1 = "Angela Yu"
name_2 = "Jack Bauer"
tr = 0
lv = 0
for c in (name_1 + name_2).upper():
    if c == 'T' or c == 'R' or c == 'U' or c == 'E':
        tr += 1
    if c == 'L' or c == 'O' or c == 'V' or c == 'E':
        lv += 1

temp = str(tr) + str(lv)
love_score = int(temp)

print(f"Your score is {love_score}.")

print()

# To count chars in world you can use count method:

combined_names = name_1 + name_2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = str(first_digit) + str(second_digit)

