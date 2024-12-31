num = int(input("Enter a number : "))

initial_num = num

num_digits = len(str(num))

sum_power = 0

for i in str(num):
    sum_power += int(i) ** num_digits

if initial_num == sum_power:
    print(f"{initial_num} is an Armstrong number")
else:
    print(f"{initial_num} is not an Armstrong")
    



