
string = input("daj: ")
copy = str()
for i in string:
    if i == "\\":
        i = "\\\\"
    copy += i
print(copy)