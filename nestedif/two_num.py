num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if num1 > num2:
    print(f"The first number {num1} is greater than {num2}")

elif num1 == num2:
    if num1 < 0:
        print("Positive")
    elif num1 > 0:
        print("Positive")
    elif num1 == 0:
        print("Zero")
    else:
        pass

else:
    print(f"The second number {num2} is grater than {num1}")


