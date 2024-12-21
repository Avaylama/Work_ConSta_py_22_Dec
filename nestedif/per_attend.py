total_days = int(input("ENter the total days of class : "))
class_attend = int(input("Enter the number of days attended : "))
class_absent = total_days - class_attend
print(F"The total number of days absent is {class_absent}")
per_class_attend = (class_attend/total_days) * 100
print(f"The percentage of class attend is {per_class_attend}%")
if per_class_attend < 75:
    print("You will not be able to sit in exam")
else:
    print("You will be able to sit in exam")
