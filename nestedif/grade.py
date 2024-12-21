grades = int(input("ENter the marks of science :"))

if grades > 80:
    print("A+")
elif grades > 60 and grades <= 80:
    print("A")
elif grades > 50 and grades <= 60:
    print("B+")
elif grades > 45 and grades <= 50:
    print("B")
elif grades > 25 and grades <= 45:
    print("C")
elif grades < 25:
    print("D")
else:
    pass
