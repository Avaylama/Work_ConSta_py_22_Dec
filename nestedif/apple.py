N = int(input("Enter the number of the students : "))
K = int(input("Enter the number of apples in basket : "))
student_apple = K // N
print(F"Each studet get {student_apple} apples")
remaining_apple = K % N 
print(f"The number of remaining apples in basket is {remaining_apple}")