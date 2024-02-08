from snake import Snake


class Lulakebab(Snake):  # class Lulakebab is child of Snake class and have all attributes and methods from super
    def __init__(self):
        super().__init__() # super invocation recommended but not strictly required


class Fish:

    def __init__(self):
        self.number_of_eye = 12

    def swimm(self):
        print("Fish swimm")


class Okon(Fish):

    def __init__(self):
        super().__init__()

    def pr(self):
        print(self.number_of_eye) # how use attributes from super

    def sw(self):
        super().swimm() # how use methods from suer



ok = Okon()

ok.pr()