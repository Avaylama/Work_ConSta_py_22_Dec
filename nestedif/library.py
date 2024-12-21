days = int(input("Enter the number of days :"))
if days <= 0:
    print("Charge wont applied")
elif days <= 5:
    charge = days * 2
    print(f"The total charge on {days} days lend is {charge}")
elif days >= 6 and days <= 10:
    charge = days * 3
    print(f"The total charge on {days} days lend is {charge}")
elif days >= 11 and days <= 15:
    charge = days * 4
    print(f"The total charge on {days} days lend is {charge}")
elif days > 15:
    charge = days * 5
    print(f"The total charge on {days} days lend is {charge}")
else:
    pass
