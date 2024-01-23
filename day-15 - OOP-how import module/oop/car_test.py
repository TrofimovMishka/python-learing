from car import Car
from wheel import Wheel
from door import Door

wheel_fl = Wheel(20)
wheel_fr = Wheel(20)
wheel_rr = Wheel(20)
wheel_rl = Wheel(20)

wheels = {wheel_fl, wheel_fr, wheel_rr, wheel_rl}

l_door = Door(300, "Red")
r_door = Door(300, "Yellow")

doors = {l_door, r_door}

car = Car(290, 70, doors, wheels)

car.drive()



