#user input
first_question = input("Does it move? ")
#left
if first_question == "yes":
  second_question = input("Should it? ")
  if second_question == "yes":
    print("no problem")
  elif second_question == "no":
    print ("duct tape")
#right
elif first_question == "no":
  second_question = input("Should it? ")
  if second_question == "no":
    print("no problem")
  elif second_question == "yes":
    print("wd-40")

  