print("Please enter the number of coins:")
quarters = int(input("# of quarters:"))
q2 = int(quarters*25)
dimes = int(input("# of dimes:"))
d2 = int(dimes*10)
nickels = int(input("# of nickels:"))
n2 = int(nickels*5)
pennies = int(input("# of pennies:"))
p2 = int(pennies*1)

dollars = int((q2+d2+n2+p2)//100)
cents = int((q2+d2+n2+p2)%100)

print("The total is", dollars, "dollars and", cents, "cents")
