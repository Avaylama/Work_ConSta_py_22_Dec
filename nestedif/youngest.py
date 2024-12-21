per1 = int(input("ENter the age of person1 :"))
per2 = int(input("ENter the age of person2 :"))
per3 = int(input("ENter the age of person3 :"))
per4 = int(input("ENter the age of person4 :"))

if per1 < per2 and per1 < per3 and per1 < 4:
    print("Person1 is youngest")
elif per2 < per3 and per2 < per4:
    print("person2 is youngest")
elif per3 < per4:
    print("person3 is youngest ")
else:
    print("person4 is youngest")