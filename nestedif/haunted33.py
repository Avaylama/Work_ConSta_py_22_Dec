print("Welcome to the Haunted House")
direction = input("Whether you want to go 'upstairs' or 'downstairs' : ").lower()
if direction == "upstairs":
    question = input("if you want to 'enter the room' say 'i' or 'stay outside' say 'o' : ").lower()
    if question == "o":
        choose = input("Choose between 'ghost', 'vampire', 'werewolf' : ").lower()
        if choose == "werewolf":
            print("You Win")
        elif choose == "ghost" or choose == "vampire":
            print("Game Over")
        else:
            print("invalid choose")
    elif question == "i":
        print("Game Over")
    else:
        print("invalid choose")
elif direction == "downstairs":
    print("Game Over")
else:
    print("invalid word")