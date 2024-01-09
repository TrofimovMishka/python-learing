import random
print("Module form list explanation in py")

list = [i for i in range(1, random.randint(1, 70), random.randint(2, 5))] # generate random sie list of numbers

list.append("bob") # no type safety
list.append("yo-ho-ho") # no type safety

print(list)

print("list in py ORDERED, index start form 0")
print(list[-1]) # get the last item

names = ['Bob', "Greg", 'Marry', 10, random] # put that you want

print(names[-3]) # third from the tail

print(names)
names[1] = 'New name fff'
print(names)
names.append('Add to the end of thi list')
print(names)

names.extend(['add', 'list', 'to list'])

print(names)

names.insert(1, 'Insert to index')
print(names)
print(len(names))


index = random.randint(0, len(names)-1)
print(f'{names[index]} is going to buy the meal today!')