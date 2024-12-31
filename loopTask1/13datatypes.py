list = [1,2,3,"d",4,5,"a"] 
integers = []
strings = []

for i in list:
    if type(i) == int:
        integers.append(i)
    elif type(i) == str:
        strings.append(i)
    else:
        pass
print("Integers :", integers)
print("Strings :", strings)