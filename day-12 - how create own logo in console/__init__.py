print("Lessons about the scope...")

var = 1


def chage_in_local_global_var():
    return var + 22


# How can change global scope without using global keyword
var = chage_in_local_global_var()
print(f'This is first print {var}')


def local_scope():
    var = 2
    print(f'This is var local scope: {var}')


def from_global_scope_1():
    print(f'This is var global 1 scope: {var}')


def from_global_scope_2():
    global var

    var = var + 10
    print(f'This is var changed in global 2 scope: {var}')


local_scope()
from_global_scope_1()
from_global_scope_2()
print(f'After func var = {var}')


#Constants

PI = 3.14159 # You plan only use UPPERCASE naming
MY_CONSTANT = 'My name'
