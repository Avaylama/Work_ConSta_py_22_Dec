print("Welcome to the Pirate Island")
direction = input("Whether you want to go 'left' say 'l' or 'right' say 'r' : ").lower()
if direction == "l":
    question = input("if you want to 'dig for tresure' say 't' or 'sail the ship' say 's' : ").lower()
    if question == "s":
        choose = input("Choose between 'shark', 'pirate ship', 'mermaid' : ").lower()
        if choose == "mermaid":
            print("You Win")
        elif choose == "shark" or "pirate ship":
            print("Game Over")
        else:
            print("invalid choose")
    elif question == "t":
        print("Game Over")
    else:
        print("invalid choose")
elif direction == "r":
    print("Game Over")
else:
    print("invalid word")