bmi = float(input("Enter the value of bmi of person : "))
if bmi < 18.5:
    print("Underweight")
elif bmi <= 18.5 and bmi < 24.9:
    print("Normal Weight")
elif bmi <= 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else:
    pass
