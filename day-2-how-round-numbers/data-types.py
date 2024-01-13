# Data types in py:

# primitives:
#Integer -> int
int_num = 10
large_num = 1222_644_888 # output -> 1222644888
print(large_num)

#Float -> float
float_num = 12.922
large_float_num = 12_333_31.92_8882
print(large_float_num) # output -> 1233331.928882

#Boolean

True
False
print(type(True)) # -> <class 'bool'>

#String
this_is_a_string = 'Bobo'

#Error
# if 10 > 9:
#     raise Exception("This is exception thown")

# print(len(145465)) # NOT valid!!!
print(len(str(145465)))

# Type casting:
print(type(int("567"))) # -> <class 'int'>

int("12")
float(12)
str(1221)

print("hello"[0]) # str represent an array of chars
