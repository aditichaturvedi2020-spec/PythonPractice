# one class but two objects

class laptop:
    brand = "acer"
    ram = "16GB"
    color = "grey"
    model = "aspire go 14"
first = laptop()      # object 
print(first.model)

laptop2 = laptop
laptop2.brand = "lenovo"
laptop2.color = "white"
laptop2.ram = "8gb"
laptop2.model = "16gen"
second = laptop2()
print(second.model)