#user input
distance_to_work = int(input("How many miles away is your workplace? "))
today_weather = (input("What's the weather today? "))
#results
if distance_to_work <= 3 and today_weather == "Sunny":
  print("You can walk to work! ")
else: 
  print("You should drive to work. ")