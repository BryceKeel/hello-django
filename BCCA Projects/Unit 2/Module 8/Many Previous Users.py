#main
def main() -> None:
  #loop
  while True:
    with open("last_user.txt", "r") as user:
      line = len(user.readlines())
      user_count = line - 1
      if user_count <= 0:
        print("You are the first user for this program!")
      elif user_count == 1:
        print(f"{user_count} user has run this program.")
      else:
        print(f"{user_count} users have run this program.")
    with open("last_user.txt", "r") as lastuser:
      for line in lastuser:
        pass
      last_line = line
      if line == 0:
        pass
      else:
        print(last_line)
    name = input("Name? ")
    with open("last_user.txt", "a") as lastuser:
      lastuser.write(f"\n{name} was the last user of this program.")

#dunder
if __name__ == "__main__":
  main()
