#initial password
passcode = (input("What's the passcode? "))
#start of loop
while True:
  action = input("[enter], [change] passcode, [quit]> ")
  #first try password
  if action == "enter":
    pw = input("What's the passcode? ")
    if pw == passcode:
      print("You can enter. ")
    else:
      print("Wrong passcode.")
#changing password
  elif action == "change":
    pw = input("What is the passcode? ")
    if pw == passcode:
      passcode = input("What should the new passcode be? ")
    else:
      print("Wrong passcode.")
  elif action == "quit":
    break
    #invalid action
  else:
    print("Invalid action.")
