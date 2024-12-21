print("Welcome to the Space Mission")
direction = input("Whether you want to go 'to the moon' say 'm' or 'to mars' say 'a' : ").lower()
if direction == "m":
    question = input("if you want to 'land on the surface' say 's' or 'stay in orbit' say 'o' : ").lower()
    if question == "o":
        choose = input("Choose between 'alien', 'asteroid', 'satellite' : ").lower()
        if choose == "satellite":
            print("You Win")
        elif choose == "alien" or "asteroid":
            print("Game Over")
        else:
            print("invalid choose")
    elif question == "s":
        print("Game Over")
    else:
        print("invalid choose")
elif direction == "a":
    print("Game Over")
else:
    print("invalid word")