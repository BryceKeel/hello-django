# Task 1: Multiply the number the user inputed by 3 and save it to a variable called day.
num = int(input("Enter a number between 1 - 10: "))
day = num * 3

# Task 2: Do 12.65 to the power of 3 rounded to the nearest whole number and save it to a variable called year.
year = int(round(12.65**3))

# Task 3: Ask the user enter a name and store it in a variable called first_name.
first_name = input("Enter a name: ")

# Task 4: Ask the user enter an adjective and store it in a variable called adjective.
adjective = input("Enter an adjective: ")

#Task 5: Ask the user to enter a type of bird and store it in a variable called type_of_bird.
type_of_bird = input("Enter a bird name: ")
#Task 6: Store the past tense of the verb run to a variable called verb_past_tense
verb_past_tense = "ran"

# Task 7: Subtract 23 from 57 and save it to a variable called num_of_stairs
num_of_stairs = 57 - 23

# Task 8: Save 0.33 to a variable called amount_1, and save 24.25 to a variable called amount_2. Multiply amount_1 with amount_2 and save the result to a variable called ounces rounded to the hundreth place.
amount_1 = 0.33
amount_2 = 24.25
ounces = round(amount_1 * amount_2, 2)

#Task 9: Ask the user to enter a price and store it in a variable called monthly_price. **Please account for cents in the price.**
monthly_price = float(input("Enter a price: "))

#Task 10: Multiply monthly_price by 12 and subtract 10 and store it in a varaible called yearly_price which should be rounded to the nearest hundredth place.
yearly_price = round((monthly_price * 12)-10, 2)

#Do not touch code below

print("")
print(
  f"It was November {day}, {year}, {first_name} woke up to the {adjective} smell of {type_of_bird} roasting in the kitchen downstairs. They {verb_past_tense} down the {num_of_stairs} stairs to see if they could help with dinner. Their mom said, 'See if your father needs a fresh drink.' So they carried a tray of {ounces} oz glasses full of lemonade into the living room. When they got there, they couldn't believe their eyes! To finish this story please subscribe for the low monthly price of ${monthly_price} or for even more savings our yearly price of ${yearly_price}."
)
