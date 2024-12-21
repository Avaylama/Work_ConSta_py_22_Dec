cp = int(input("ENter the cost price of bike"))
if cp > 100000:
    total_cptax = cp * (15/100)
    print(f"With 15% road tax, it is {total_cptax} in amount")
elif cp > 50000 and cp <=100000:
    total_cptax = cp * (10/100)
    print(f"With 10% road tax, it is {total_cptax} in amount")
elif cp <= 50000:
    total_cptax = cp * (5/100)
    print(f"With 5% road tax, it is {total_cptax} in amount")
else:
    print("No Tax")
