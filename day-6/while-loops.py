a = 60

while a > 50:
    print(a)
    a -= 1
    if a == 55:
        break
else:
    print('In else')  # use 'else' if loop break occur - means if break will work - else not work!!!

for i in range(5):
    print(f'number = {i}')
    if i == 7:
        break
else:
    print('For loop In else')  # use 'else' if loop break occur - means if break will work - else not work!!!
