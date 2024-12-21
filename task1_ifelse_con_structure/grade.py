marks = int(input("Enter the marks :"))
if marks < 25:
    print("grade : F")
elif marks == 25 and marks < 45:
    print("grade : E")
elif marks == 45 and marks < 50:
    print("grade : D")
elif marks == 50 and marks < 60:
    print("grade : C")
elif marks == 60 and marks < 80:
    print("grade : B")
elif marks == 80 and marks > 80:
    print("grade : A")
else:
    print("Invalid")




