class vehicle:
    def __init__(self,color):
        self.color = color
        print("cute vehicle")
class car(vehicle):
     def car(self):
        print("the color is: ", self.color)
veh = car("pink")
print(veh.color)      # method call
veh.car()             # to call init