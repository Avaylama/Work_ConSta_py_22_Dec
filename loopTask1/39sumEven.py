even_add = 0
odd_add = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_add += i
    else:
        odd_add += i

print(f"The sum of even numbers is {even_add}")
print(f"The sum of odd numbers is {odd_add}")
