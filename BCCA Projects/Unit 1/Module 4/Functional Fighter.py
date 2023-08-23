# Simplified version of a past student project:
# https://github.com/BaseCampCoding/Seth-JeremiahT

import random

#player
def input_pokemon_type():
  while True:
    player_type = input("Please choose   from these types: ").title()
    if (player_type == "Fire" or player_type == "Grass"
        or player_type == "Rock" or player_type == "Ice"
        or player_type == "Ground"):
      return player_type
      break
    else:
      print("Please choose a valid type!")
  

#enemy
def random_pokemon_type():
  enemy_type_number = random.randint(0, 4)
  if enemy_type_number == 0:
    enemy_type = "Fire"
    return enemy_type
  elif enemy_type_number == 1:
    enemy_type = "Grass"
    return enemy_type
  elif enemy_type_number == 2:
    enemy_type = "Rock"
    return enemy_type
  elif enemy_type_number == 3:
    enemy_type = "Ice"
    return enemy_type
  elif enemy_type_number == 4:
    enemy_type = "Ground"
    return enemy_type

#main function
def main():
  print("""Here are your choices: 
  Fire
  Grass
  Rock
  Ice
  Ground
  
  Remember:
      Fire beats grass and ice 
      Grass beats rock and ground
      Rock beats fire and ice
      Ice beats grass and ground
      Ground beats fire and rock!""")

  player_health = 100
  enemy_health = 100

  while player_health > 0 and enemy_health > 0:
    player_type = input_pokemon_type()
    enemy_type = random_pokemon_type()

    if player_type == enemy_type:
      print(f"You both chose {player_type}! It's a tie!")
    else:
      has_fire_advantage = (player_type == "Fire"
                            and (enemy_type == "Grass" or enemy_type == "Ice"))
      has_grass_advantage = (player_type == "Grass" and
                             (enemy_type == "Rock" or enemy_type == "Ground"))
      has_rock_advantage = (player_type == "Rock"
                            and (enemy_type == "Fire" or enemy_type == "Ice"))
      has_ice_advantage = (player_type == "Ice" and
                           (enemy_type == "Grass" or enemy_type == "Ground"))
      has_ground_advantage = (player_type == "Ground" and
                              (enemy_type == "Fire" or enemy_type == "Rock"))
      has_player_advantage = (has_fire_advantage or has_grass_advantage
                              or has_rock_advantage or has_ice_advantage
                              or has_ground_advantage)

      if has_player_advantage:
        print(f"The computer chose {enemy_type}! You win!")
        enemy_health -= random.randint(10, 30)
      else:
        print(f"The computer chose {enemy_type}! You lose!")
        player_health -= random.randint(10, 30)

    print(f"Player health: {player_health}")
    print(f"Computer health: {enemy_health}")

  if player_health <= 0:
    print("You were defeated by the computer!\n")
  elif enemy_health <= 0:
    print("You defeated the computer!\n")

#dunder
if __name__ == "__main__":
  main()
