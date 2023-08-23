#player name
def is_on_team(name):
  if name == "Carol" or name == "Nick" or name == "Maureen":
    return True
  else:
    return False
#rick
def rick_shakes(name,won):
  if name == "Carol" and won == True or name == "Nick" and won == False or name == "Maureen" and won == True:

    return False
  else:
    return True
    #john
def john_shakes(name,won):
  if name == "Carol" and won == True or name == "Nick" and won == False or name == "Maureen" and won == True:

    return True
  else:
    return False
    #Jared
def jared_shakes(name, won):
  if name != "Nick":
    return True
#main code
def main():
  name = input("Name: ")

  if is_on_team(name):
    did_win = input("Did you win? ") == "Yes"

    if rick_shakes(name, did_win):
      print("Rick: shakes hand")
    else:
      print("Rick: ...")

    if john_shakes(name, did_win):
      print("John: shakes hand")
    else:
      print("John: ...")

    if jared_shakes(name, did_win):
      print("Jared: shakes hand")
    else:
      print("Jared: ...")
  else:
    print("You weren't even on the team!")

#running code
if __name__ =="__main__":
  main()