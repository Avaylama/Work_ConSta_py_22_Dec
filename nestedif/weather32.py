weather = input("Enter the season name : ").lower()
if weather == "sunny":
    print("Do outdoor activities like hiking or a picnic")
elif weather == "rainy":
    decision = input(f"if you have raincoat or umbrella?\n if yes, write 'yes' and if no write 'no'")
    if decision == "yes":
        print("Go nearby mall or museum")
    elif decision == "no":
        print("Stay home and watching movies")
    else:
        pass
else:
    pass

