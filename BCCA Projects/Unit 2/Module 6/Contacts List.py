from dataclasses import dataclass
from typing import List

@dataclass
class Contact:
  name: str
  email: str
  phone: str
  favorite: bool

#create
def create(contacts: List[Contact])-> None:
  name=input("Name: ")
  email=input("email: ")
  phone=input("Phone: ")
  while True:
   favorite=input("favorite: ")
   if favorite == "yes":
    favorite=True
    break
   elif favorite =="no":
    favorite=False
    break
   else:
     print("invalid input")

  contact=Contact(name,email,phone,favorite)
  contacts.append(contact)
#view all
def view_all(contacts: List[Contact])->None:
  if not contacts:
    print("Contact not found")
  else:
    for contact in contacts:
      if contact.favorite == True:
        favorite= "Favorite"
      else:
        favorite= "Not Favorite"
      print(contact.name,contact.email,contact.phone,favorite, sep=' - ')

#view favorite
def view_favorite(contacts: List[Contact])->None:
  if not contacts:
    print("Contact not found")
  else:
    for contact in contacts:
      if contact.favorite == True:
        favorite = "Favorite"
        print(f"{contact.name} - {contact.email} - {contact.phone} ")

#view name
def view_name(contacts: List[Contact])->None:
  user_search= input("Name: ")

  for contact in contacts:
    if contact.name==user_search:
      if contact.favorite == True:
        favorite = "Favorite"
      else:
        favorite = "Not Favorite"
      print(f"{contact.name} - {contact.email} - {contact.phone} - {favorite}")

  print("Contact not found")
#update
def update(contacts: List[Contact])-> None:
  name = input("Name: ")

  for contact in contacts:
    if contact.name==name:
      email=input("New Email: ")
      phone=input("New Phone: ")
      favorite = input("Favorite? ").lower()
      if favorite == "yes":
        contact.favorite = True
    
      elif favorite=="no":
        contact.favorite=False
      contact.email = email
      contact.phone= phone
      return
  print("Contact not found")

def delete(contacts: List[Contact]) ->None:
  name=input("Name: ")
  for contact in contacts:
    if contact.name == name:
      contacts.remove(contact)
      return
  print("Contact not found")

#main
def main() -> None:
  contact=[]
  while True:
    user=input("[create], view [all], view by [name], view [favorites], [update], [delete], or [quit]? ")
    if user=="create":
      create(contact)
    elif user=="all":
      view_all(contact)
    elif user=="favorites":
      view_favorite(contact)
    elif user=="name":
      view_name(contact)
    elif user== "update":
      update(contact)
    elif user=="delete":
      delete(contact)
    elif user=="quit":
      break
    else:
      print("Invalid action")
#runs main
if __name__=='__main__':
  main()