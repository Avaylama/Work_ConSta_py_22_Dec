print("Welcome to the Wizarding World")
choose = input("Choose subject between 'spells' or 'potions' : ").lower()
if choose == "spells":
    ques = input("Do you want to 'practice magic' as 'm' or 'complete in duels' as 'd' : ").lower()
    if ques == "m":
        print("You masterred a powerful spell. You Win!")
    elif ques == "d":
        print("You lost ot a rival wizard. Game Over.")
    else:
        pass
elif choose == "potions":
    ques = input("Do you want to 'brew an elixir' as 'e' or 'create poison' as 'p' : ").lower()
    if ques == ("e"):
        print("You healed a village. You Win!")
    elif ques == ("p"):
        print("Your potion backfires. Game Over.")
    else:
        pass
else:
    pass
