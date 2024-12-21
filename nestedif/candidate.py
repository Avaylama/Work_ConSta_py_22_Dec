age = int(input("Enter the age of candidate : "))
degree = False
work_experience = int(input("Enter the work experience : "))
if age >= 18 and degree == True:
    if work_experience > 3:
        print("Highly Eligible")
    elif work_experience >= 1 and work_experience <= 3:
        print("Eligible")
    elif work_experience < 1:
        print("Under Review")
    else: 
        pass
elif age < 18:
    print("Not Eligible")
else:
    pass

