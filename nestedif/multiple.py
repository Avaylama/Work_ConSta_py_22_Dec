num = int(input("ENter the number : "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 3 != 0 and num % 5 == 0:
    print("Buzz")
elif num % 3 != 0 and num % 5 != 0:
    print("Buzz")
else:
    pass


