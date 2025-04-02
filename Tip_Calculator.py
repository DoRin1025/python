
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
people = int(input("Hos many people to split the bill? "))

procent = tip / 100 + 1
tip_total = bill * procent / people

print(round(tip_total, 2))
