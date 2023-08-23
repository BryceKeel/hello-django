#user input
pepper = input ("Would you like some pepper? ")
#internal
amount = 0
while True:
  pepper = input("More? ")
  if pepper == "yes":
    amount = amount + 1
  elif pepper == "no":
    break
  else:
    print("Invalid Input")
#output
if amount > 0 and amount < 3:
  print("You have a little pepper on your salad.")
elif amount > 2:
  print("You have a lot of pepper on your salad.")
else:
  print("You have no pepper on your salad.")
