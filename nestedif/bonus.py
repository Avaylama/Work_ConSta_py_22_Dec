time = int(input("Enter the time services of employee"))
if time > 10:
    print(f"You got 10% bonus")
elif time >= 6 and time <= 10:
    print(f"You got 8% bonus")
elif time < 6:
    print(f"You got 5% bonus")
else:
    pass


