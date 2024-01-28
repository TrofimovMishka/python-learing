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
        return self


user = User(12, 88)

user2 = user.get_instance()  # => return a reference to the object
print(user2.get_age())

user2.set_age(10000)   # => change a value in a original object

print(user.get_age())
