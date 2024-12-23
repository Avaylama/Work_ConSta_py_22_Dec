print("Welcome to the Pirate Ship Adventure")
choose = input("choose between 'searches for treasure' as 't' or 'battle enemy ships' as 'b' : ").lower()
if choose == 't':
    ques = input("Do you want to 'dig on the island' as 'i' or 'explore the cave' as 'c' : ").lower()
    if ques == "i":
        print("You found a hidden treasure chest. You Win!")
    elif ques == "c":
        print("You were trapped inside. Game Over.")
    else:
        pass
elif choose == 'b':
    ques = input("Do you want to 'attack' or 'defend' : ").lower()
    if ques == "attack":
        print("You won the battle. You Win!")
    elif ques == "defend":
        print("You were iutnumbered. Game Over.")
    else:
        pass
else:
    pass
