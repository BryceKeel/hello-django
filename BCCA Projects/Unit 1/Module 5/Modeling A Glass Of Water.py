#dataclass
from dataclasses import dataclass

@dataclass
class Glass:
  capacity: int
  current_amount: int
#pour in 
def pour_in(glass: Glass, amount_of_water: int) -> None:
  if glass.current_amount + amount_of_water <= glass.capacity:
    glass.current_amount += amount_of_water
  else:
    glass.current_amount = glass.capacity
#pour out
def pour_out(glass: Glass, amount_of_water: int) -> None:
  if glass.current_amount - amount_of_water >= 0:
    glass.current_amount -= amount_of_water
  else:
    glass.current_amount = 0
#main
def main():
  capacity = int(input("Capacity? "))
  dataglass = Glass(capacity, 0)
 
  while True:
    print(f"Glass capacity: {dataglass.capacity}" )
    print(f"Glass amount: {dataglass.current_amount}")
    action = input("Pour [in], pour [out], or [quit]? ")
    if action == "in":
      plusdatamount = int(input("Amount? "))
      pour_in(dataglass, plusdatamount)
    elif action == "out":
      minusdatamount = int(input("Amount? "))
      pour_out(dataglass, minusdatamount)
    elif action == "quit":
      break



if __name__ == "__main__":
  main()