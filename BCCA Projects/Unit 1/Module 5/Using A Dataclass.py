from dataclasses import dataclass


@dataclass
class Cat:
    name: str
    is_hungry: bool

#cat sound
def cat_sound(cat: Cat) -> str:
    if cat.is_hungry:
        return "hiss"
    else:
        return "meow"

#feed cat
def feed_cat(cat: Cat) -> None:
    cat.is_hungry = False
#start of code
def main():
  Kit = Cat("Kit", True)
  Kat = Cat("Kat", True)
  while True:
    print("Kit says", cat_sound(Kit))
    print("Kat says", cat_sound(Kat))
    print("Feed [Kit], Feed [Kat], [quit]")
    directive = input("> ").upper()

    if directive == "KAT":
      feed_cat(Kat)
    elif directive == "KIT":
      feed_cat(Kit)
    elif directive == "QUIT":
      break

    else:
      print("Please provide a valid cat name or quit.")


if __name__ == "__main__":
  main()