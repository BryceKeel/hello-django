from typing import Dict


#input
def input_action() -> str:
  while True:
    actions = ("books", "author", "quit")
    useraction = input("view [books], show [author], [quit]> ")
    if useraction in actions:
      return useraction
    else:
      print("Please provide a valid action.")


#print books
def print_books(book_authors: Dict[str, str]) -> None:
  for name in book_authors:
    print(f"- {name}")


#input book
def input_book(book_authors: Dict[str, str]) -> str:
  while True:
    user = input("book> ")
    if user in book_authors:
      return user
    else:
      print("Please provide a valid book.")


#author name
def print_author(book_authors: Dict[str, str]) -> None:
  user = input_book(book_authors)
  print(book_authors[user])


#main
def main() -> None:
  book_authors = {
    'Harry Potter': 'JK Rowling',
    'Effective Testing with RSpec 3': 'Myron Marston',
    'Automate the Boring Stuff': 'Al Sweigart',
    'Quiet': 'Susan Cain',
    'Peak': 'Anders Ericsson',
  }

  while True:
    useraction = input_action()
    if useraction == "books":
      print_books(book_authors)
    elif useraction == "author":
      print_author(book_authors)
    else:
      break


#dunder
if __name__ == "__main__":
  main()
