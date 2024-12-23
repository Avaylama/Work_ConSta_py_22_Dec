age = int(input("ENter your age : "))
if age >= 21 and age <= 35:
    gender = input("Enter your gender if 'male' enter 'M' and if 'female' enter 'F' : ").upper()
    if gender == "M":
        experience = int(input("ENter your experience : "))
        if experience >= 5:
            print("Senior Developer")
        elif experience < 5:
            print("Junior Developer")
        else:
            pass
    elif gender == "F":
        experience = int(input("ENter your experience : "))
        if experience >= 5:
            print("Senior Analyst")
        elif experience < 5:
            print("Junior Analyst")
        else:
            pass
elif age > 35:
    gender = input("Enter your gender if 'male' enter 'M' and if 'female' enter 'F' : ").upper()
    if gender == "M" or gender == "F":
        print("Manager Role")
else:
    pass



    
