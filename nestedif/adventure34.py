print("Welcome to the Jungle Adventure")
direction = input("Enter the direction you want to go 'left' or 'right' : ")
if direction == "left":
    question = input("if you want to 'climb a tree' say 'c' or 'explore the cave' say 'e' : ").lower()
    if question == "e":
        choose = input("Choose between 'bear', 'tiger', 'snake' : ").lower()
        if choose == "snake":
            print("You Win")
        elif choose == "bear" or "tiger":
            print("Game Over")
        else:
            print("invalid choose")
    elif question == "c":
        print("Game Over")
    else:
        print("invalid choose")
elif direction == "right":
    print("Game Over")
else:
    print("invalid word")