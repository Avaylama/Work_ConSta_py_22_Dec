sub1 = int(input("ENter the marks of science :"))
sub2 = int(input("ENter the marks of english :"))
sub3 = int(input("ENter the marks of nepali :"))
sub4 = int(input("ENter the marks of maths :"))
sum = sub1 + sub2 + sub3 + sub4
per = (sum * 100)/4
if per >= 70:
    print("Distinction")
elif per >= 60:
    print("First")
elif per >= 40:
    print("pass")
elif per < 40:
    print("Fail")
else:
    pass