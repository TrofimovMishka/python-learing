import random
import new_module

print("In day 4 will learn Random module and lists in py")

print(random.randint(1, 99901)) # pseudo random int number
print(random.randrange(1, 121299901, 7)) # pseudo random int number

new_module.my_funck(random.random()) # pseudo number between 0.0 and 1.0 exclude this numbers
new_module.my_funck(random.random() * 9) # pseudo number between 0.0 and 9.0 exclude this numbers


