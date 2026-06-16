# countdown for New Year

import time
x = int(input("enter the number: "))

print(" Countdown starts now ! ")

for num in range(x, 0, -1):
    print(num)
    time.sleep(1)
print("Happy New Year!! ")