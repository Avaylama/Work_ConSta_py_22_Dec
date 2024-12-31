string = input("Enter the string : ")
space = 0

for i in range(len(string)):
    space_count = string[:i+1].count(' ')

print(f"The number of space in the string is {space_count}")