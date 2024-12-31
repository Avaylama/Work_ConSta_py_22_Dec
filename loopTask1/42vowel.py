string = input("Enter a string : ").lower()

vowels = "aeiou"

new_string = ""

for i in string:
    if i not in vowels:
        new_string += i

print(new_string)

