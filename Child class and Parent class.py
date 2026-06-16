class vehicle():
    def start(self):
        print("vehicle is starting")
class car(vehicle):
    def drive(self):
        print("big car wow")
class bike(vehicle):
    def ride(self):
        print(" bike is starting")
obj1 = car
obj1.car()
obj1.bike()