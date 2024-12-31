bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
good = ""

for i in string:
    if i not in bad_chars and i != " ":
        good += i
print(good)
