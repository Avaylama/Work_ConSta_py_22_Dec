num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
if num1 % 2 == 0 and num2 % 2 == 0:
    cal = num1 + num2
    print(f"The sum of {num1} and {num2} is {cal}")
elif (num1 % 2 == 0 or num2 % 2 == 0) and (num1 % 2 != 0 or num2 % 2 != 0):
    if num1 >= num2:
        cal1 = num1 - num2
        print(f"The difference between {num1} and {num2} is {cal1}")
    elif num2 >= num1:
        cal2 = num2 - num1
        print(f"The difference between {num2} and {num1} is {cal2}")
    else:
        pass
else:
    cal = num1 * num2
    print(f"The product of {num1} and {num2} is {cal}")
