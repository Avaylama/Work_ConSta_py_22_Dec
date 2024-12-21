service_time = int(input("Enter the year of services : "))
if service_time > 5:
    salary = int(input("Enter the salary amount of a month : "))
    bonus = salary * (5/100)
    net_bonus = bonus * 12
    print(f"The net bonus amount is {net_bonus}")
else:
    print("You are not eligible for bonus")