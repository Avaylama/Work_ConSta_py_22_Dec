ques = input("Are you vegetarian 'v' or non-vegetarian 'n': ")
if ques == "v":
    ask = input("Do you want 'Salad' or 'Pasta' ").lower()
    if ask == "salad":
        print("Salad")
    elif ask == "pasta":
        print("Pasta")
    else:
        pass
elif ques == "n":
    ask = input("Do you want 'Chicken' or 'Fish' : ").lower()
    if ask == "chicken":
        print("Chicken")
    elif ask == "Fish":
        print("Fish")
    else:
        pass
else:
    pass