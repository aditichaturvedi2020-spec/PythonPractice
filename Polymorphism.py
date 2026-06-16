class dog:
    def sound(self):
        print("baking")
class cat:
    def sound(self):
        print("meow")
class cow:
    def sound(self):
        print("moo")
animals = [cow(), cat(), dog()]
for a in animals:
    a.sound()