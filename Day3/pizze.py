print("Welcome to Python Pizza Deliveries")
s_pizza = 15
m_pizza = 20
l_pizza = 25
total = 0
size = input("What size pizza do you want? S, M or L ")
pepperoni = input("Do you wnat pepperoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    total = s_pizza

elif size == "M":
    total = m_pizza

elif size == "L":
    total = l_pizza

else:
    print(f"You tiped the wrong inputs")

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total +=1

print(f"Your finall bill is {total}")


