skin = input("enter your skin type: ")

if skin == "oily":
    print("Wash your face with gentle cleanser.\n For moisturizer: Apply oil free moisturizer. ")
    print("At last apply susncreen.")
elif skin == "dry": 
    print("Wash your face with gentle cleanser.")
    print("To avoid flakiness apply thick layer of moisturizer")
    print("At last apply susncreen.")
elif skin == "combination":
    print("Wash your face with gentle cleanser and oil free moisturizer ")
    print("At last apply sunscreen.")
elif skin == "sensitive":
    print("Wash your face with gentle cleanser and apply non comedogenic moisturizer,")
    print("AT last sunscreen that suits you")
else:
    print("First know your skintype, Anything else would you like to ask")
