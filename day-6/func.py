import random

def my_func(name, sur_name):
    print(f'Hello {name} {sur_name}')


def req_func_return():
    if random.randint(1, 56) > 3:
        print("bob")
        if random.randint(1, 56) < 20:
            print('Hi')
        else:
            print('Hohh')
    else:
        print('PPPPPP')
    return 12 + random.randint(1, 56)



my_func('bob', 'Hey')

print(req_func_return())
