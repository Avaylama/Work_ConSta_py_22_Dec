print("Welcome to the Space Adventure")
choose = input("Choose beteen 'land on Mars' as 'm' or 'fly to jupiter' as 'j' : ").lower()
if choose == "m":
    ask = input("Do you want to 'explore' as 'e' or 'build a base' as 'b' : ").lower()
    if ask == "e":
        print("You found alien artifacts. You Win!")
    elif ask == "b":
        print("You ran out of resource. Game Over.")
    else:
        pass
elif choose == "j":
    print("Your spaceship crached. Game Over.")
else:
    pass