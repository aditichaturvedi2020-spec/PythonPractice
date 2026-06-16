#check if live word is present in the file

file = open("certification.txt","r")
data = file.read()

if "live" in data:
    print("yes its there!")
else:
    print("No")