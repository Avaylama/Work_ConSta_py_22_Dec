first_num = 7 
second_num = 9
operator = input("Enter the operator '+'")
if operator == "+":
    cal = first_num + second_num
    print(f"the sum is {cal}")
elif operator == "-":
    cal = first_num - second_num
    print(f"the subtract is {cal}")
elif operator == "*":
    cal = first_num * second_num
    print(f"the multiply is {cal}")
elif operator == "/":
    cal = first_num / second_num
    print(f"the divide is {cal}")
else:
    pass
