print("Let's start work with dictionary")

# Dictionary example

my_dict = {"a": "Bob", 'b': 12, 1: 'Hello number'}

# <<<<<<<<<<< How retrieve data from dictionary? >>>>>>>>>>>>>>

print(my_dict['a'])  # key is a str
print(my_dict.get("b"))
print(my_dict.get(1))

print(f'Items of dict: {my_dict.items()}')
print(f'Keys of dict: {my_dict.keys()}')
print(f'Values of dict: {my_dict.values()}')

# <<<<<<<<<<< How add key-value pair to dictionary? >>>>>>>>>>>>>>

my_dict["new_key"] = 'This is new value'

print(my_dict)

# <<<<<<<<<<< How edit item in dict? >>>>>>>>>>>>>>

my_dict["a"] = 'HAHHAAHHA'
print(my_dict)

# <<<<<<<<<<< How loop through dictionary? >>>>>>>>>>>>>>
# This loop through keys:
for i in my_dict:
    print(f"For loop {i}")

# This loop through values:
for i in my_dict.values():
    print(f"For loop values {i}")

# This loop through items -> list (key, value):
for i in my_dict.items():
    print(f"For loop values {i}")

# <<<<<<<<<<< How create empty dictionary? >>>>>>>>>>>>>>

empty_dict = {}

# <<<<<<<<<<< Wipe (clear) existing dictionary >>>>>>>>>>>>>>

my_dict = {}

print(my_dict)