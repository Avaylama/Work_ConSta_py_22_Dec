price = int(input("Enter the price of an item"))
if price > 1000:
    discount = (10/100) * price
    final_price = price - discount
    print(f"With applied 10% ({discount}) discount, it is {final_price}")
elif price > 500:
    discount = (5/100) * price
    final_price = price - discount
    print(f"With applied 5% ({discount}) discount, it is {final_price}")
else:
    pass
