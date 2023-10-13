import random

response= input("Enter you want to roll a dice?")
response="y"

while response=="y":
    no = random.randint(1, 6)
    print("Dice: ")
    print("  -------")

    if (no == 1):
        print("  |     |")
        print("  |  o  |")
        print("  |     |")
    elif no  == 2:
            print("  | o   |")
            print("  |     |")
            print("  |   o |")
    elif no == 3:
            print("  | o   |")
            print("  |  o  |")
            print("  |   o |")
    elif no == 4:
            print("  | o o |")
            print("  |     |")
            print("  | o o |")
    elif no == 5:
            print("  | o o |")
            print("  |  o  |")
            print("  | o o |")
    else: 
            print("  | o o |")
            print("  | o o |")
            print("  | o o |")
    print("  -------")

if (response=="n"):
    print("Goodbye")
        
    

   
    