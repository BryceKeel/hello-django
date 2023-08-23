from dataclasses import dataclass
from typing import List

@dataclass
class Spider:
  name: str
  secret_identity: str
  universe: str
  awareness: bool

#create
def create(spiders: List[Spider])-> None:
  name=input("Spider Name: ")
  secret_identity=input("Secret Identity: ")
  universe=input("Universe: ")
  while True:
   awareness=input("Aware Of Spider-Verse: ")
   if awareness == "yes":
    awareness=True
    break
   elif awareness =="no":
    awareness=False
    break
   else:
     print("invalid input")

  spider=Spider(name,secret_identity,universe,awareness)
  spiders.append(spider)
#view all
def view_all(spiders: List[Spider])->None:
  if not spiders:
    print("Spider not found")
  else:
    for spider in spiders:
      if spider.awareness == True:
        awareness= "Aware Of Spider-Verse"
      else:
        awareness= "Not Aware of Spider-Verse"
      print(spider.name,spider.secret_identity,spider.universe,awareness, sep=' - ')

#view favorite
def view_favorite(spiders: List[Spider])->None:
  if not spiders:
    print("Spider not found")
  else:
    for spider in spiders:
      if spider.awareness == True:
        awareness = "Aware Of Spider-Verse"
        print(f"{spider.name} - {spider.secret_identity} - {spider.universe} ")

#view name
def view_name(spiders: List[Spider])->None:
  user_search= input("Name: ")

  for spider in spiders:
    if spider.name==user_search:
      if spider.awareness == True:
        awareness = "Aware Of Spider-Verse"
      else:
        awareness = "Not Aware Of Spider-Verse"
      print(f"{spider.name} - {spider.secret_identity} - {spider.universe} - {awareness}")

  print("Spider not found")
#update
def update(spiders: List[Spider])-> None:
  name = input("Name: ")

  for spider in spiders:
    if spider.name==name:
      secret_identity=input("New Secret Identity: ")
      universe=input("New Spider-Verse: ")
      awareness = input("Aware of Spider-Verse ").lower()
      if awareness == "yes":
        spider.awareness = True
    
      elif awareness=="no":
        spider.awareness=False
      spider.secret_identity = secret_identity
      spider.universe= universe
      return
  print("Spider not found")
#delete
def delete(spiders: List[Spider]) ->None:
  name=input("Name: ")
  for spider in spiders:
    if spider.name == name:
      spiders.remove(spider)
      return
  print("Spider not found")

#main
def main() -> None:
  spider=[]
  while True:
    user=input("[create], view [all], view by [name], view [aware], [update], [delete], or [quit]? ")
    if user=="create":
      create(spider)
    elif user=="all":
      view_all(spider)
    elif user=="favorites":
      view_favorite(spider)
    elif user=="quit":
      break

    elif user=="name":
      view_name(spider)

    elif user== "update":
      update(spider)
    elif user=="delete":
      delete(spider)
    else:
      print("Invalid action")
#runs main
if __name__=='__main__':
  main()