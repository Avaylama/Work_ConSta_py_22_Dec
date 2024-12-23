temp = float(input("ENter the temperature in celcius : "))
if temp > 40:
    print("Hot")
elif temp > 20 and temp < 40:
    print("Warm")
elif temp < 20:
    print("Cold")
else:
    pass
