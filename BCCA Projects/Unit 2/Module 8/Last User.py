def main():
  #first user
    with open("last_user.txt" , "r") as lastuser:
      firstuser = lastuser.read()
      if firstuser == "":
        print("You are the first user of this program!")
        #takes name
        name = input("Name? ")
        with open("last_user.txt" , "w") as user:
          user.write(name)
      else:
        with open("last_user.txt" , "r") as f:
          lastuser = f.read()
        print(f"{lastuser} was the last user of this program.")
        #take name
        newname = input("Name? ")
        with open("last_user.txt" , "w") as user:
          user.write(newname)
if __name__== "__main__":
  main()
  