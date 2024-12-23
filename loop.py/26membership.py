age = int(input("Enter the age : "))
if age >= 18 and age < 30:
    gender = input("Enter you gender if 'male' enter 'M' or if 'female' enter 'F' : ").upper()
    if gender == "M":
        membership = input("Whether you want 'monthly' or 'yearly' : ").lower()
        if membership == "monthly":
            print("The price for monthly subscription is Rs 50.")
        elif membership == "yearly":
            print("The price for yearly subscription is Rs 500.")
        else:
            pass
    elif gender == "F":
        membership = input("Whether you want 'monthly' or 'yearly' : ").lower()
        if membership == "monthly":
            print("The price for monthly subscription is Rs 45.")
        elif membership == "yearly":
            print("The price for yearly subscription is Rs 450.")
        else:
            pass
elif age >= 30 and age <= 50:
    gender = input("Enter you gender if 'male' enter 'M' or if 'female' enter 'F' : ").upper()
    if gender == "M" or gender == "F":
        membership = input("Whether you want 'monthly' or 'yearly' : ").lower()
        if membership == "monthly":
            print("The price for monthly subscription is Rs 60.")
        elif membership == "yearly":
            print("The price for yearly subscription is Rs 600.")
        else:
            pass
elif age > 50:
    gender = input("Enter you gender if 'male' enter 'M' or if 'female' enter 'F' : ").upper()
    if gender == "M" or gender == "F":
        membership = input("Whether you want 'monthly' or 'yearly' : ").lower()
        if membership == "monthly":
            print("The price for monthly subscription is Rs 40.")
        elif membership == "yearly":
            print("The price for yearly subscription is Rs 400.")
        else:
            pass
    
        
    
        