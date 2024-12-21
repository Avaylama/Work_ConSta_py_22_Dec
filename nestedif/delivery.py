weight = int(input("Enter the weight of the package : "))
if weight < 5:
    charge = 5 * weight
    print(f"The delivery cost for {weight} Kg package is {charge}")
elif weight >=5 and weight < 20:
    charge = 10 * weight
    print(f"The delivery cost for {weight} Kg package is {charge}")
elif weight > 20:
    charge = 20 * weight
    print(f"The delivery cost for {weight} Kg package is {charge}")
else:
    pass    