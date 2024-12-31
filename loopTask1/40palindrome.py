num = int(input("Enter a number : "))

initial_num = num
reversed_num = 0

count_num = len(str(num))

for _ in range(count_num):
    last_digit = num % 10

    reversed_num = reversed_num * 10 + last_digit

    num = num // 10

if initial_num == reversed_num:
    print(f"{initial_num} is a palindrome")
else:
    print(f"{initial_num} is not a palindrome")