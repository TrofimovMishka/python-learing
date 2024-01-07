# round(number, precision)
print(round(1 / 3, 4))
print(round(3 // 2, 1))
print(round(3 // 2, 1))

print(3/2) # -> 1.5
print(int(3/2)) # -> 1


#
a = 12
b = 2
a += b # accept -= /= *=
print(a)

# f string example
score = 0
height = 1.4
is_good = True

print(f"your score {score}, and height is {height}, but a question is: Is this good? {is_good}")

#Life in weeks
age = input('Type your age: \n')
# 48 or 52 - depend on from year
weeks = (90 - int(age)) * 52
print(f"You have {weeks} weeks left.")

#Error will occures
age = 12
# print("you " + age + " old") #-> TypeError: can only concatenate str (not "int") to str