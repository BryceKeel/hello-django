#user input
coin = input("Coins: ")
print("")
pennies = 0
nickels = 0
dimes = 0
quarters = 0
i = 0
#identiers
while i < len(coin):
  if coin [i] == "P":
    pennies += 1
    i += 1
  elif coin [i] == "N":
    nickels  += 1
    i += 1
  elif coin [i] == "D":
    dimes += 1
    i += 1
  elif coin [i] == "Q":
    quarters += 1
    i += 1
#math
total = (pennies * .01) + (nickels * .05) + (dimes * .10) + (quarters * .25)
print(f"""
Summary
Pennies: {pennies}
Nickels: {nickels}
Dimes: {dimes}
Quarters: {quarters}
Total: ${total:.2f}
""")