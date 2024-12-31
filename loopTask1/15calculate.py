string = input("Enter the string : ")

letters = 0
digits = 0
spaces = 0

for i in string:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        pass

print("Letters :", letters)
print("Digits :", digits)
print("Spaces :", spaces)


