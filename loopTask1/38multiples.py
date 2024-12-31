sum = 0

for i in range(3, 99):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(f"The sum of multiples of 3 or 5 is {sum}")