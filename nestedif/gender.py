age = int(input("ENter the age : "))
gender = input("Enter the gender('M'for male and 'F' for female)").upper()
days = int(input("Enter the number of days : "))
if age >= 18 and age < 30:
    if gender == "M":
        wage = 700 * days
        print(f"The wage for male age between (18-29)  is {wage}")
    elif gender == "F":
        wage = 750 * days
        print(f"The wage for female age between (18-29)  is {wage}")
    else:
        pass
elif age >= 30 and age <= 40:
    if gender == "M":
        wage = 800 * days
        print(f"The wage for male age between (30-40)  is {wage}")
    elif gender == "F":
        wage = 850 * days
        print(f"The wage for female age between (30-40)  is {wage}")
    else:
        pass
else:
    pass