#greeting
print("Welcome to Count your Blessings!")
#list
blessings = []


#add funcion
def add_blessing() -> None:
  thankful_for = input("\nEnter something you are thankful for: ")
  blessings.append(thankful_for)


#remove function
def remove_blessing() -> None:
  not_thankful_for = input("\nWhich item would you like to delete? ")
  if not_thankful_for in blessings:
    blessings.remove(not_thankful_for)
  else:
    print("This item is not in your Thankful Box!")


#update function
def update_blessing(old_item, new_item):
  if old_item in blessings:
    updateindex = blessings.index(old_item)
    blessings[updateindex] = new_item


#view function
def view_blessings() -> None:
  print(f"\nYou are thankful for the following {len(blessings)} item(s):")
  num = 0
  for blessing in blessings:
    num += 1
    print(f"{num}. {blessing}")


#main function
def main():
  while True:
    action = input(
      "\n[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: "
    )
    if action == "Add":
      add_blessing()
    elif action == "Remove":
      remove_blessing()
    elif action == "Update":
      old_item = input("\nWhich item would you like to update? ")
      if old_item in blessings:
        new_item = input("What is your new item? ")
        update_blessing(old_item, new_item)
      else:
        print("This item is not in your Thankful Box!")
    elif action == "View":
      view_blessings()
    elif action == "q":
      break
    else:
      print("invalid input")


#dunder
if __name__ == "__main__":
  main()
