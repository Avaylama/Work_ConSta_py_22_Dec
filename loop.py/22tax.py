age = int(input("Enter the age : "))
if age >= 18 and age < 60:
    gender = input("ENter gender if 'male' as 'M' or if 'female' as 'F' : ").upper()
    if gender == "M":
        income = int(input("Enter the income : "))
        if income > 1000000:
            tax = (30/100) * income
            final_salary = income - tax
            print(f"With 30% (rs{tax}) tax, the final_salary is {final_salary}")
        elif income > 500000 and income < 1000000:
            tax = (20/100) * income
            final_salary = income - tax
            print(f"With 20% (rs{tax}) tax, the final_salary is {final_salary}")
        elif income <= 500000:
            tax = (5/100) * income
            final_salary = income - tax
            print(f"With 5% (rs{tax}) tax, the final_salary is {final_salary}")
        else:
            pass
    if gender == "F":
        income = int(input("Enter the income : "))
        if income > 1000000:
            tax = (25/100) * income
            final_salary = income - tax
            print(f"With 25% (rs{tax}) tax, the final_salary is {final_salary}")
        elif income > 500000 and income < 1000000:
            tax = (15/100) * income
            final_salary = income - tax
            print(f"With 15% (rs{tax}) tax, the final_salary is {final_salary}")
        elif income <= 500000:
            tax = (5/100) * income
            final_salary = income - tax
            print(f"With 5% (rs{tax}) tax, the final_salary is {final_salary}")
        else:
            pass
elif age >= 60:
    gender = input("ENter gender if 'male' as 'M' or if 'female' as 'F' : ").upper()
    if gender == "M" or gender == "F":
        income = int(input("Enter the income : "))
        if income > 1000000:
            tax = (20/100) * income
            final_salary = income - tax
            print(f"With 20% (rs{tax}) tax, the final_salary is {final_salary}")
        elif income <= 1000000:
            tax = (10/100) * income
            final_salary = income - tax
            print(f"With 10% (rs{tax}) tax, the final_salary is {final_salary}")
        else:
            pass
else:
    pass

        


            
    