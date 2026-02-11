sentence=input("enter a string:")
string=" "
for ch in sentence:
    if ch not in string:
        string+=ch
print("sentence after removing duplicate:",string)        