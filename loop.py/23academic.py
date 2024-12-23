age = int(input("Enter your age : "))
if age >= 18 and age <= 25:
    gender = input("Enter your gender if 'male' enter 'M' and if 'female' enter 'f'F : ").upper()
    if gender == "M":
        score = int(input("Enter your score : "))
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        elif score < 70:
            print("No Scholarship")
        else:
            pass
    elif gender == "F":
        score = int(input("Enter your score : "))
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        elif score < 65:
            print("No Scholarship")
        else:
            pass
else: 
    pass