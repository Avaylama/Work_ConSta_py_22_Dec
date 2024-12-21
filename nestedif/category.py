percentage = int(input("Enter the percentage : "))
if percentage < 40:
    print("Failed")
elif percentage >= 40 and percentage < 55:
    print("Fair")
elif percentage >= 55 and percentage < 65:
    print("Good")
elif percentage >= 65:
    print("Excellent")
else:
    pass
