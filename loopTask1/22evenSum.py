first = int(input("Enter the starting number : "))
last = int(input("Enter the ending number : "))

sum = 0

for i in range(first, last + 1):
    if i % 2 == 0:
        sum += i
print(f"The sum of even number between {first} and {last} number is {sum}")