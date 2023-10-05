str = input()
newStr = ""

if len(str) >= 1 and len(str) <= 20:
    for i in str:
        if i.islower():
            newStr += i.upper()
        else:
            newStr += i.lower()
print(newStr)