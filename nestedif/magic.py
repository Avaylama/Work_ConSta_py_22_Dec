print("Welcome to the Magic Forest")
direction = input("Enter the direction you want to go 'north' or 'south' : ")
if direction == "north":
    question = input("if you want to 'cross the river' say 'c' or 'follow the path' say 'f' : ").lower()
    if question == "f":
        choose = input("Choose between 'fairy', 'ogre', 'elf' : ").lower()
        if choose == "elf":
            print("You Win")
        elif choose == "ogre" or "fairy":
            print("Game Over")
        else:
            print("invalid choose")
    elif question == "c":
        print("Game Over")
    else:
        print("invalid choose")
elif direction == "south":
    print("Game Over")
else:
    print("invalid word")