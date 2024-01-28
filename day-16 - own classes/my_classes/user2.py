class User:

    def __init__(self, age, hands):
        self.age = age
        self.hands = hands

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_hands(self, hands):
        self.hands = hands

    def get_instance(self):
        return User(1, 1)


user = User(12, 88)

user2 = user.get_instance()  # => return a new Object

print(user2.get_age())

user2.set_age(10000)   # => change a value of a new object

print(user.get_age())
print(user2.get_age())
