salary = int(input("Enter the monthly salary : "))
if salary > 50000:
    print("High Earner")
elif salary > 20000 and salary <= 50000:
    print("Mid Earner")
else:
    print("Low Earner")
