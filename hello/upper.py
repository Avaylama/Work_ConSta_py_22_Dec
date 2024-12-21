char = input("ENter the character :")
if char.isupper():
    print(f"The entered character {char} is in uppercase")
elif char.islower():
    print(f"The entered character {char} is in lowecase")
elif char.isdigit():
    print(f"The entered character {char} is in digit")
else:
    print("Enter the character again")

