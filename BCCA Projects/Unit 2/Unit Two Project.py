from dataclasses import dataclass



@dataclass
class Pokemon:
  type: str


unova_pokemon = {
  "Victini": Pokemon(["Psychic"]),
  "Snivy": Pokemon(["Grass"]),
  "Servine": Pokemon(["Grass"]),
  "Serperior": Pokemon(["Grass"]),
  "Tepig": Pokemon(["Fire"]),
  "Pignite": Pokemon(["Fire"]),
  "Emboar": Pokemon(["Fire"]),
  "Oshawott": Pokemon(["Water"]),
  "Dewott": Pokemon(["Water"]),
  "Samurott": Pokemon(["Water"]),
  "Patrat": Pokemon(["Normal"]),
  "Watchog": Pokemon(["Normal"]),
  "Lillipup": Pokemon(["Normal"]),
  "Herdier": Pokemon(["Normal"]),
  "Stoutland": Pokemon(["Normal"]),
  "Purrloin": Pokemon(["Dark"]),
  "Liepard": Pokemon(["Dark"]),
  "Pansage": Pokemon(["Grass"]),
  "Simisage": Pokemon(["Grass"]),
  "Pansear": Pokemon(["Fire"]),
  "Simisear": Pokemon(["Fire"]),
  "Panpour": Pokemon(["Water"]),
  "Simipour": Pokemon(["Water"]),
  "Munna": Pokemon(["Psychic"]),
  "Musharna": Pokemon(["Psychic"]),
  "Pidove": Pokemon(["Normal"]),
  "Tranquill": Pokemon(["Normal"]),
  "Unfezant": Pokemon(["Normal"]),
  "Blitzle": Pokemon(["Electric"]),
  "Zebstrika": Pokemon(["Electric"]),
  "Roggenrola": Pokemon(["Rock"]),
  "Boldore": Pokemon(["Rock"]),
  "Gigalith": Pokemon(["Rock"]),
  "Woobat": Pokemon(["Psychic"]),
  "Swoobat": Pokemon(["Psychic"]),
  "Drilbur": Pokemon(["Ground"]),
  "Excadrill": Pokemon(["Ground"]),
  "Audino": Pokemon(["Normal"]),
  "Timburr": Pokemon(["Fighting"]),
  "Gurdurr": Pokemon(["Fighting"]),
  "Conkeldurr": Pokemon(["Fighting"]),
  "Tympole": Pokemon(["Water"]),
  "Palpitoad": Pokemon(["Water"]),
  "Seismitoad": Pokemon(["Water"]),
  "Throh": Pokemon(["Fighting"]),
  "Sawk": Pokemon(["Fighting"]),
  "Sewaddle": Pokemon(["Bug"]),
  "Swadloon": Pokemon(["Bug"]),
  "Leavanny": Pokemon(["Bug"]),
  "Venipede": Pokemon(["Bug"]),
  "Whirlipede": Pokemon(["Bug"]),
  "Scolipede": Pokemon(["Bug"]),
  "Cottonee": Pokemon(["Grass"]),
  "Whimsicott": Pokemon(["Grass"]),
  "Petilil": Pokemon(["Grass"]),
  "Lilligant": Pokemon(["Grass"]),
  "Basculin": Pokemon(["Water"]),
  "Sandile": Pokemon(["Ground"]),
  "Krokorok": Pokemon(["Ground"]),
  "Krookodile": Pokemon(["Ground"]),
  "Darumaka": Pokemon(["Fire"]),
  "Darmanitan": Pokemon(["Fire"]),
  "Maractus": Pokemon(["Grass"]),
  "Dwebble": Pokemon(["Bug"]),
  "Crustle": Pokemon(["Bug"]),
  "Scraggy": Pokemon(["Dark"]),
  "Scrafty": Pokemon(["Dark"]),
  "Sigilyph": Pokemon(["Psychic"]),
  "Yamask": Pokemon(["Ghost"]),
  "Cofagrigus": Pokemon(["Ghost"]),
  "Tirtouga": Pokemon(["Water"]),
  "Carracosta": Pokemon(["Water"]),
  "Archen": Pokemon(["Rock"]),
  "Archeops": Pokemon(["Rock"]),
  "Trubbish": Pokemon(["Poison"]),
  "Garbodor": Pokemon(["Poison"]),
  "Zorua": Pokemon(["Dark"]),
  "Zoroark": Pokemon(["Dark"]),
  "Minccino": Pokemon(["Normal"]),
  "Cinccino": Pokemon(["Normal"]),
  "Gothita": Pokemon(["Psychic"]),
  "Gothorita": Pokemon(["Psychic"]),
  "Gothitelle": Pokemon(["Psychic"]),
  "Solosis": Pokemon(["Psychic"]),
  "Duosion": Pokemon(["Psychic"]),
  "Reuniclus": Pokemon(["Psychic"]),
  "Ducklett": Pokemon(["Water"]),
  "Swanna": Pokemon(["Water"]),
  "Vanillite": Pokemon(["Ice"]),
  "Vanillish": Pokemon(["Ice"]),
  "Vanilluxe": Pokemon(["Ice"]),
  "Deerling": Pokemon(["Normal"]),
  "Sawsbuck": Pokemon(["Normal"]),
  "Emolga": Pokemon(["Electric"]),
  "Karrablast": Pokemon(["Bug"]),
  "Escavalier": Pokemon(["Bug"]),
  "Foongus": Pokemon(["Grass"]),
  "Amoonguss": Pokemon(["Grass"]),
  "Frillish": Pokemon(["Water"]),
  "Jellicent": Pokemon(["Water"]),
  "Alomomola": Pokemon(["Water"]),
  "Joltik": Pokemon(["Bug"]),
  "Galvantula": Pokemon(["Bug"]),
  "Ferroseed": Pokemon(["Grass"]),
  "Ferrothorn": Pokemon(["Grass"]),
  "Klink": Pokemon(["Steel"]),
  "Klang": Pokemon(["Steel"]),
  "Klinklang": Pokemon(["Steel"]),
  "Tynamo": Pokemon(["Electric"]),
  "Eelektrik": Pokemon(["Electric"]),
  "Eelektross": Pokemon(["Electric"]),
  "Elgyem": Pokemon(["Psychic"]),
  "Beheeyem": Pokemon(["Psychic"]),
  "Litwick": Pokemon(["Ghost"]),
  "Lampent": Pokemon(["Ghost"]),
  "Chandelure": Pokemon(["Ghost"]),
  "Axew": Pokemon(["Dragon"]),
  "Fraxure": Pokemon(["Dragon"]),
  "Haxorus": Pokemon(["Dragon"]),
  "Cubchoo": Pokemon(["Ice"]),
  "Beartic": Pokemon(["Ice"]),
  "Cryogonal": Pokemon(["Ice"]),
  "Shelmet": Pokemon(["Bug"]),
  "Accelgor": Pokemon(["Bug"]),
  "Stunfisk": Pokemon(["Ground"]),
  "Mienfoo": Pokemon(["Fighting"]),
  "Mienshao": Pokemon(["Fighting"]),
  "Druddigon": Pokemon(["Dragon"]),
  "Golett": Pokemon(["Ground"]),
  "Golurk": Pokemon(["Ground"]),
  "Pawniard": Pokemon(["Dark"]),
  "Bisharp": Pokemon(["Dark"]),
  "Bouffalant": Pokemon(["Normal"]),
  "Rufflet": Pokemon(["Normal"]),
  "Braviary": Pokemon(["Normal"]),
  "Vullaby": Pokemon(["Dark"]),
  "Mandibuzz": Pokemon(["Dark"]),
  "Heatmor": Pokemon(["Fire"]),
  "Durant": Pokemon(["Bug"]),
  "Deino": Pokemon(["Dark"]),
  "Zweilous": Pokemon(["Dark"]),
  "Hydreigon": Pokemon(["Dark"]),
  "Larvesta": Pokemon(["Bug"]),
  "Volcarona": Pokemon(["Bug"]),
  "Cobalion": Pokemon(["Steel"]),
  "Terrakion": Pokemon(["Rock"]),
  "Virizion": Pokemon(["Grass"]),
  "Tornadus": Pokemon(["Flying"]),
  "Thundurus": Pokemon(["Electric"]),
  "Reshiram": Pokemon(["Dragon"]),
  "Zekrom": Pokemon(["Dragon"]),
  "Landorus": Pokemon(["Ground"]),
  "Kyurem": Pokemon(["Dragon"]),
  "Keldeo": Pokemon(["Water"]),
  "Meloetta": Pokemon(["Normal"]),
  "Genesect": Pokemon(["Bug"])
}




current_team = []


def create():
  global current_team
  current_team = []
  print("You have started a new team.")
  add()


def add():
    if len(current_team) >= 6:
        print("Your team is already full. You cannot add more Pokémon.")
        return

    print("Available Unova Pokemon:")
    for dexnum, (name, pokemon) in enumerate(unova_pokemon.items(), start=1):
        print(f"{dexnum}. {name}")

    try:
        choice = int(input("Enter the number corresponding to the Pokemon you want to add: "))
        if 1 <= choice <= len(unova_pokemon):
            pokemon_name = list(unova_pokemon.keys())[choice - 1]
            if pokemon_name not in current_team:
                current_team.append(pokemon_name)
                print(f"{pokemon_name} has been added to your team!")
            else:
                print(f"{pokemon_name} is already in your team.")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")





def remove():
  if not current_team:
    print("Your team is empty. Nothing to remove.")
    return

  print("Your Current Team:")
  for dexnum, pokemon_name in enumerate(current_team, start=1):
    print(f"{dexnum}. {pokemon_name}")

  try:
    choice = int(
      input(
        "Enter the number corresponding to the Pokemon you want to remove: "))
    if 1 <= choice <= len(current_team):
      removed_pokemon = current_team.pop(choice - 1)
      print(f"{removed_pokemon} has been removed from your team.")
    else:
      print("Invalid choice. Please enter a valid number.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")



def replace():
  if not current_team:
    print("Your team is empty. Nothing to replace.")
    return

  print("Your Current Team:")
  for dexnum, pokemon_name in enumerate(current_team, start=1):
    print(f"{dexnum}. {pokemon_name}")

  try:
    choice = int(
      input(
        "Enter the number corresponding to the Pokemon you want to replace: "))
    if 1 <= choice <= len(current_team):
      removed_pokemon = current_team.pop(choice - 1)
      add()
      print(f"{removed_pokemon} has been replaced in your team.")
    else:
      print("Invalid choice. Please enter a valid number.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")




def view():
  if not current_team:
    print("Your team is empty.")
  else:
    print("Your Current Team:")
    for dexnum, pokemon_name in enumerate(current_team, start=1):
      print(f"{dexnum}. {pokemon_name}")



def save():
  if not current_team:
    print("Your team is empty. Nothing to save.")
    return

  try:
    team_name = input("Enter a name for your team: ")
    with open(f"{team_name}.txt", "w") as file:
      for pokemon_name in current_team:
        file.write(f"{pokemon_name}\n")
    print("Your team has been saved successfully.")
  except Exception as e:
    print(f"Error occurred while saving the team: {e}")




def view_old():
  try:
    team_name = input("Enter the name of the team you want to view: ")
    with open(f"{team_name}.txt", "r") as file:
      old_team = [line.strip() for line in file]
      if not old_team:
        print(f"Team '{team_name}' is empty or does not exist.")
      else:
        print(f"Old Team '{team_name}':")
        for dexnum, pokemon_name in enumerate(old_team, start=1):
          print(f"{dexnum}. {pokemon_name}")
  except FileNotFoundError:
    print(f"Team '{team_name}' does not exist.")
  except Exception as e:
    print(f"Error occurred while viewing the old team: {e}")




def main():
  while True:
    print("""
▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ 　 ▒█░▒█ ▒█▄░▒█ ▒█▀▀▀█ ▒█░░▒█ ░█▀▀█ 　 ▀▀█▀▀ ▒█▀▀▀ ░█▀▀█ ▒█▀▄▀█ 
▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ 　 ░▒█░░ ▒█░░▒█ 　 ▒█░▒█ ▒█▒█▒█ ▒█░░▒█ ░▒█▒█░ ▒█▄▄█ 　 ░▒█░░ ▒█▀▀▀ ▒█▄▄█ ▒█▒█▒█ 
▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ 　 ░▒█░░ ▒█▄▄▄█ 　 ░▀▄▄▀ ▒█░░▀█ ▒█▄▄▄█ ░░▀▄▀░ ▒█░▒█ 　 ░▒█░░ ▒█▄▄▄ ▒█░▒█ ▒█░░▒█ 

▒█▀▀█ ▒█░▒█ ▀█▀ ▒█░░░ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ 
▒█▀▀▄ ▒█░▒█ ▒█░ ▒█░░░ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄█ ░▀▄▄▀ ▄█▄ ▒█▄▄█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█

""")
    first_actions = input("Would you like to [create] a team?, or [q]uit? ")
    if first_actions == "create":
      create()
      while True:
        print(f"""


░█████╗░██╗░░░██╗██████╗░██████╗░███████╗███╗░░██╗████████╗  ████████╗███████╗░█████╗░███╗░░░███╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██╔██╗██║░░░██║░░░  ░░░██║░░░█████╗░░███████║██╔████╔██║
██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║░░░██║░░░  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██║░╚███║░░░██║░░░  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

""")
        second_actions = input(
          "Do you want to [add] to your current team, [remove] from your current team, [replace] something on your current team, [view] your current team, [call] an old team, [save] your current team, or [q]uit? "
        )
        if second_actions == "add":
          add()
        elif second_actions == "remove":
          remove()
        elif second_actions == "replace":
          replace()
        elif second_actions == "view":
          view()
        elif second_actions == "save":
          save()
        elif second_actions == "call":
          print(f"""

░█████╗░██╗░░░░░██████╗░  ████████╗███████╗░█████╗░███╗░░░███╗
██╔══██╗██║░░░░░██╔══██╗  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
██║░░██║██║░░░░░██║░░██║  ░░░██║░░░█████╗░░███████║██╔████╔██║
██║░░██║██║░░░░░██║░░██║  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
╚█████╔╝███████╗██████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░╚════╝░╚══════╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
""")
          view_old()

        elif second_actions == "q":

          break
        else:
          print("Invalid action.")
      else:
        print("Please provide a valid action.")
    elif first_actions == "q":
      print("You didn't create a team.")
      break
    else:
      print("Please provide a valid action")


if __name__ == "__main__":
  main()
