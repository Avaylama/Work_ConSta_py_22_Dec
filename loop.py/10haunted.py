print("Welcomr to the Underwater World")
choose = input("Choice between 'enter the castle' as 'c' and 'run away' as 'r' : ").lower()
if choose == "c":
    pick = input("Pick among 'red', 'green', 'black' : ").lower()
    if pick == "red":
        print("You entered a room full of flames. Game Over.")
    elif pick == "green":
        print("You found the treasure. You Win!")
    elif pick == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        pass
elif choose == "r":
    print("You escaped safely")
else:
    pass