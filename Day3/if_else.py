
height = int(input("Waht is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your ege?"))
    if age < 12:
        bill = 1
        print("Please pay 1$")
    elif age >= 12 and age < 18:
        bill = 7
        print("Plaese pay 7$")
    else:
        bill = 12
        print("Please pay 12$")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No")
    if wants_photo == "y":
        bill += 3
    
    print(f"You final bill is {bill}")
else:
    print("Sorry you have to grow taller bedore yum can ride ")