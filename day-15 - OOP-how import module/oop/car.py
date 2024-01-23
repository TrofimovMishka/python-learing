class Car:
    speed = 0
    fuel = 0
    door = []
    wheel = []

    def __init__(self, speed, fuel, door, wheel):
        self.speed = speed
        self.fuel = fuel
        self.door = door
        self.wheel = wheel

    def get_speed(self):
        return self.speed

    def drive(self):
        print(f"the car drive with speed {self.speed}")

    def get_doors(self):
        return len(self.door)
