list = [1, 2, 3, 4]
add = []

for i in list:
    if i == 2:
        add.append("a")
    elif i == 3:
        add.append(2)
    else:
        add.append(i)
print(add)