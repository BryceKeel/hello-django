#Count
def count(user) -> None:
  if user == "1":
    print(MODULES[0])
  if user == "2":
    print(MODULES[1])
  if user == "3":
    print(MODULES[2])
  if user == "4":
    print(MODULES[3])
  if user == "5":
    print(MODULES[4])
  if user == "6":
    print(MODULES[5])
  if user == "7":
    print(MODULES[6])
  if user == "8":
    print(MODULES[7])
  if user == "9":
    print(MODULES[8])
  if user == "10":
    print(MODULES[9])
  else: 
    print("invalid module number")
#modules
MODULES = (
    "Basic User Interaction",
    "Branching",
    "Repetition",
    "Functions",
    "Dataclass",
    "List/Sets/Tuples",
    "Dictionaries",
    "Searching and sorting",
    "Persistence/SQL",
    "OOP",
)

#main
def main() -> None:
  while True:
      user = input("> ")
      count(user)
   

#dunder
if __name__ == "__main__":
    main()
