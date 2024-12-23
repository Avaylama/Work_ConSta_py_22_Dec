age = int(input("Enter the age : "))
if age < 12:
    gender = input("Enter your gender if 'male' enter 'M' and if 'female' enter 'F' : ").upper()
    if gender == "M":
        ques = input("Whether they choose 'matinee' or 'evening' : ").lower()
        if ques == "matinee":
            print("The ticket price is Rs 800")
        elif ques == "evening":
            print("The ticket price is Rs 100")
        else:
            pass
    elif gender == "F":
        ques = input("Whether they choose 'matinee' or 'evening' : ").lower()
        if ques == "matinee":
            print("The ticket price is Rs 700")
        elif ques == "evening":
            print("The ticket price is Rs 900")
        else:
            pass
elif age >= 60:
    gender = input("Enter your gender if 'male' enter 'M' and if 'female' enter 'F' : ").upper()
    if gender == "M" or gender == "F":
        print("The ticket price is Rs 600")
else:
    pass

