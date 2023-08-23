#Display welcome message
print("Welcome to Good Burger.")
print("Home of the Good Burger.")
print("Can I take your order?\n")

#Ask for user input

number_of_burgers = int(input("Good Burgers ($4.50):"))
number_of_fries = int(input(" French Fries ($1.50):"))
number_of_drinks = int(input(" Drinks       ($1.00): "))

#Mathematical Operations

price_of_burgers = float(number_of_burgers * 4.50)
price_of_fries = float(number_of_fries * 1.50)
price_of_drinks = float(number_of_drinks * 1.00)
total = price_of_burgers + price_of_fries + price_of_drinks

#Display receipt

print("")
print("Here is your receipt:")
print("- Good Burgers $4.50 x " + str(number_of_burgers), end=" = $")
print("%.2f" % (price_of_burgers))
print("- French Fries $1.50 x " + str(number_of_fries), end=" = $")
print("%.2f" % (price_of_fries))
print("- Drinks       $1.00 x " + str(number_of_drinks), end=" = $")
print("%.2f" % (price_of_drinks))
print("TOTAL", end=" = $")
print("%.2f" % (total))
