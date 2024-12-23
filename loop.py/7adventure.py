print("Welcome to the Forest Adventure")
choose_path = input("Choose between 'left' or 'right' : ").lower()
if choose_path == "left":
    pick = input("Pick between 'explore' or 'rest' : ").lower()
    if pick == "explore":
        print("You found treasure!")
    elif pick == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        pass
elif choose_path == "right":
    print("You fell into a trap. Game Over.")
else:
    pass