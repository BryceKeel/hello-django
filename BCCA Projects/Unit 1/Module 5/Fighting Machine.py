#dataclass
from dataclasses import dataclass
import random

#inputtype
def input_pokemon_type() -> str:
    while True:
      player_type = input("Please choose from these types: ").title()
      if is_valid_type(player_type):
        return player_type
        break
      else:
        print("Please choose a valid type!")

#valid?
def is_valid_type(player_type: str) -> bool:
    if player_type != ["Fire", "Grass","Rock", "Ice", "Ground"]:
      return True
    else:
      return False

#enemy
def random_pokemon_type() -> str:
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

#advantage
def has_advantage(player_type: str, enemy_type: str) -> bool:
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
    return True
  else:
    return False
    


### ^^^ Functions you should already have  ^^^
###     I just don't want to include the
###     solutions so that someone can't
###     just look ahead and cheat.
### ------------------------------------------
### vvv New stuff you should have to write vvv


@dataclass
class Game:
    player_health: int
    enemy_health:int

#greet
def print_greeting() -> None:
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
      Ground beats fire and rock!
      """)

#gameover
def is_game_over(game: Game) -> bool:
    if game.player_health == 0:
      return True
    else:
      return False


def play_round(game: Game) -> None:
    player_type = input_pokemon_type()
    enemy_type = random_pokemon_type()
    if player_type == enemy_type:
      print(f"You both chose {player_type}! It's a tie!")
    else:
      if has_advantage(player_type, enemy_type):
        print(f"The computer chose{enemy_type}!You win!")
        game.enemy_health -= random.randint(10,30)
      else:
        print(f"The computer chose {enemy_type}! You Lose!")
        game.player_health -= random.randint(10,30)

#pdead
def is_player_dead(game: Game) -> bool:
    if game.player_health <= 0:
      return True
    else:
      return False

#edead
def is_computer_dead(game: Game) -> bool:
    if game.enemy_health <= 0:
      return True
    else:
      return False

#main
def main():
    print_greeting()

    game = Game(100, 100)

    while not is_game_over(game):
        play_round(game)
        print(f"Player health: {game.player_health}")
        print(f"Enemy health: {game.enemy_health}")

        if is_player_dead(game):
          print("You were defeated by the computer!\n")
          break
        elif is_computer_dead(game):
          print("You defeated the computer!\n")
          break


if __name__ == '__main__':
    main()
