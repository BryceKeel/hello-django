from dataclasses import dataclass

@dataclass
class Counter:
  number: int
#inc
def increase(counter: Counter) -> None:
  counter.number += 1

#dec
def decrease(counter: Counter) -> None:
  counter.number -= 1 
#main
def main():
  count = Counter(0)
  while True:
    print(f"Count: {count.number}")
    numer = input("[inc], [dec], [quit]> ")
    if numer == "inc":
      increase(count)
    elif numer == "dec":
      decrease(count)
    elif numer == "quit":
      break
    
if __name__ == "__main__":
  main()
