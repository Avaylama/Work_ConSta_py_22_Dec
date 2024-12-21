current_balance = 10000
print("1. Balance check")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")
choice = int(input("Enter the choice number between (1-4) : "))
if choice == 1:
    print(f"Your courrent balance is {current_balance}")
elif choice == 2:
    amount = int(input("Enter the amount to be withdraw : "))
    if amount > current_balance:
        print("Insufficient balance")
    else:
        current_balance = current_balance - amount
        print(f"The withdrawn amount is {amount}")
        print(f"The remaining amount is {current_balance}")
elif choice == 3:
    amount = int(input("Enter the amount to be deposit : "))
    if amount <= 0:
        print("invalid amount.  enter positive number")
    else:
        current_balance = current_balance + amount
        print(f"The Deposit amount is {current_balance}")
elif choice == 4:
    print("Reenter again the from start")
else:
    print("Thank you for visiting")