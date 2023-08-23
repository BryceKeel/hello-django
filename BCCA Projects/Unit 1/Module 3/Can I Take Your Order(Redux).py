#greeting
print("""Welcome to Good Burger.
Home of the Good Burger.
Can I take your order? """) 
#ordering
good_burgers = input("Good Burgers ($4.50): ")
while good_burgers .isdigit() == False:
  print("Please type a positive integer. ")
  good_burgers = input("Good Burgers ($4.50): ")
  if good_burgers.isdigit()==True:
    if good_burgers.isdigit()<0:
      print("Please type a positive integer")
      good_burgers = input(("Good Burgers ($4.50): "))
good_burgers = int(good_burgers)
fries = input("French Fries ($1.50): ")
while fries .isdigit() == False:
  print("Please type a positive integer. ")
  fries = input("French Fries ($1.50): ")
  if fries.isdigit()==True:
    if fries.isdigit()<0:
      print("Please type a positive integer")
      fries = input(("French Fries ($1.50): "))
fries = int(fries)
drinks = input("Drinks ($1.00): ")
while drinks .isdigit() == False:
  print("Please type a positive integer. ")
  drinks = input("Drinks ($1.00): ")
  if drinks.isdigit()==True:
    if drinks.isdigit()<0:
      print("Please type a positive integer")
      drinks = input(("Drinks ($1.00): "))
drinks = int(drinks)
#price
burgerCost = good_burgers * 4.5
friesCost = fries * 1.5
drinksCost = drinks * 1
total = burgerCost + friesCost + drinksCost
#recipt
print(f"""
Here is your receipt:
- Good Burgers $4.5 x {good_burgers} = ${burgerCost:.2f}
- French Fries $1.5 x {fries} = ${friesCost:.2f}
- Drinks       $1.0 x {drinks} = ${drinksCost:.2f}
TOTAL = ${total:.2f}
""")