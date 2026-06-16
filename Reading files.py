# read entire file

with open("report.txt","r") as f:
    data = f.read()
    print(data)

# read line by line
with open("report.txt","r") as f:
    line4 = f.readline()
    line3 = f.readline()
    print("line4 ", line4)
    print("line 3 is :", line3)