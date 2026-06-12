#slicing in python

str1 = "fundamentals"

print(str1[0:5]) #5th letter got excluded
print(str1[6:8]) #8th letter got excluded

#food name and print middle 3 characters and last 2 characters

str = input("favourite food: ")
middle = len(str)//2  

output1 = str[middle-1:middle+2]
print("you will get", output1)
