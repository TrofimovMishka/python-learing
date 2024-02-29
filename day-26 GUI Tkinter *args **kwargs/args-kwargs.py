def add(*args): # how get any numbers of arguments
    print(args) #tuple => ('bob', 3, 'hello')
    print(type(args)) # <class 'tuple'>

    for i in args:
        print(i)

add("bob", 3, "hello")


def kwa(**kwargs): # named arguments ( key word arguments )
    print(kwargs) # {'first': 12, 'next': 'hell'}
    print(type(kwargs)) # <class 'dict'>

kwa(first=12, next="hell") # name of the variables must be


def combine(*args, **kwargs):
    for i in args:
        print(i)

    # print(kwargs["bob"]) # throw KeyError: 'bob' if key not exist
    print(kwargs.get("bob")) # return nun and no errors occurred

#and now you can use and/or
combine(12, 4)
combine(bob="Hello")
combine(12, 44, bob="Hello")

def multi(a, *args, **kwargs):
    print(a, args, kwargs)

multi(1, 4, 5, 78,  bob= "Hello", goog=12) # 1 (4, 5, 78) {'bob': 'Hello', 'goog': 12}

# Advanced py arguments **kwargs, *args
def example(name=..., bob=..., gift="Hello"):
    print("name= " + name)
    print(bob) # Ellipsis
    print("gift= " + gift)

example("Fix")

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car = Car(make=True)
print(car.model) # None


