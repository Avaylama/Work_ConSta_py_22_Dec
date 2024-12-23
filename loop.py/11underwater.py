print("Welcome to the Underwater World")
choose = int(input("choose between 'dive deeper' as 'd' or 'surface' as 's' : ")).lower()
if choose == "d":
    ques = input("Do you want to 'search for pearls' as 'p' or 'chase the fish' as 'f' : ").lower()
    if ques == "p":
        print("You found a rare pearl. You Win!")
    elif ques == "f":
        print("You got lost underwater. Game Over.")
    else:
        pass
elif choose == "s":
    print("You returned safely.")
else:
    pass

