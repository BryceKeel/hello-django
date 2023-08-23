print("""Welcome to 20.. err.. 3 questions!

This is the game where I tell you which Pokemon Game you are thinking of.

Here are your choices:
Red/Blue
Gold/Silver
Ruby/Sapphire
Diamond/Pearl
Black/White
X/Y
Sun/Moon
Sword/Shield
""")

ds = input("Was it on the DS? [Y/N] ")
if ds == "Y":
    threed = input("Is it 3D? [Y/N] ")
    if threed == "Y":
        human = input("Does it have chibi sprites? [Y/N] ")
        if human == "Y":
            print("Your game is X/Y")
        else:
            print("Your game is Sun/Moon")
    else:
        male = input("Is the game super slow? [Y/N] ")
        if male == "Y":
            print("Your game is Diamond/Pearl")
        else:
            print("Your game is Black/White")
else:
    gameboy = input("Is the game on the original Gameboy [Y/N] ")
    if gameboy == "Y":
        bugs = input("Does the game have a large amount of bugs? [Y/N] ")
        if bugs == "Y":
            print("Your game is Red/Blue")
        else:
            print("Your game is Gold/Silver")
    else:
        switch = input("Is the game on the Nintendo Switch? [Y/N] ")
        if switch == "Y":
            print("Your game is Sword/Shield")
        else:
            print("Your game is Ruby/Sapphire")