#read
def read():
  favorite = input("Favorite> ")
  try: 
    with open (f"{favorite}.txt" , "r") as fav:
      print(f"{favorite} is {fav.read()}")
  except FileNotFoundError:
    print(f"You have not saved a favorite {favorite}")
#write
def write():
  favorite = input("Favorite> ")
  favitem = input(f"Favorite {favorite}> ")
  with open (f"{favorite}.txt" , "w") as fav:
    fav.write(favitem)
    print(f"Wrote {favitem} as favorite {favorite}")
    fav.close()
#main
def main():
  while True:
    actions = input("[read], [write], [quit]> ")
    if actions == "read":
      read()
    elif actions == "write":
      write()
    elif actions == "quit":
      break
    else:
      print("Invalid Action")

#dunder
if __name__ == "__main__":
  main()
