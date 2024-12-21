income = int(input("Enter the income of user : "))
credit_score = int(input("Enter the credit score : "))

if income > 50000:
    if credit_score > 700:
        print("Loan approved")
    elif credit_score >= 600 and credit_score <= 700:
        print("Loan approved with highest interest rate")
    elif credit_score < 600:
        print("Loan disapproved")
elif income < 50000:
    print("Loan disapproved")
else:
    pass