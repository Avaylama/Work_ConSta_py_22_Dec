list = [1,2,3,"d",4,5,"a"] 
integers = []
strings = []

for i in list:
    if type(i) == int:
        integers.append(type(i))
    elif type(i) == str:
        strings.append(type(i))
    else:
        pass
print("Integers Types :", integers)
print("Strings Types :", strings)