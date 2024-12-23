price = int(input("Enter the price of an item : "))
if price > 1000:
    dis = (20/100)*price
    new_price = price - dis
    print(f"With apllying 20% (rs{dis}) discount, the new price is {new_price}")
elif price > 500 and price < 1000:
    dis = (10/100)*price
    new_price = price - dis
    print(f"With apllying 10% (rs{dis}) discount, the new price is {new_price}")
elif price < 500:
    print("No discount")
else:
    pass