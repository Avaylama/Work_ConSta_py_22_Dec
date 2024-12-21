# import math
a = int(input("Enter the number of student in 1st class : "))
b = int(input("Enter the number of student in 2nd class : "))
c = int(input("Enter the number of student in 3rd class : "))
class1 = round((a+1) // 2)
class2 = round((b+1) // 2)
class3 = round((c+1) // 2)

# class1 = math.ceil(a / 2)
# class2 = math.ceil(b / 2)
# class3 = math.ceil(c / 2)

cal = class1 + class2 + class3
print(f"Minimal desk needed for class a is {class1}")
print(f"Minimal desk needed for class b is {class2}")
print(f"Minimal desk needed for class c is {class3}")
print(f"total desk needed for whole 3 class is {cal}")


    

