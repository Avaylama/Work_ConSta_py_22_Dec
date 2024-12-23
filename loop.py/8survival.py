print("Welcome to the Jungle Survival Challenge")
ques = input("Do you want to 'search for food' as 's' and 'build a shelter' as 'b' : ").lower()
if ques == "s":
    choose = input("Choose between 'hunt' or 'gather' : ").lower()
    if choose == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choose == "gather":
        print("You found enough food. You Win!.")
    else:
        pass
elif ques == "b":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    pass