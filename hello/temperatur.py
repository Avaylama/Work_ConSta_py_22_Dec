temp = float(input("Enter the temperature :"))
if temp > 30:
    print("It's hot, stay hydrated!")
elif temp >= 15 and temp <= 30:
    print("Enjoy the weather!")
elif temp < 15:
    print("It's cold, wear warm clothes!")
else:
    pass