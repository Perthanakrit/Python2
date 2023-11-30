# abcdefghijk
# abcde
txt = input()

first_half = txt[(len(txt)//2)-1::-1]
last_half = ""
center = ""

if len(txt) % 2 != 0:
    last_half = txt[:(len(txt)//2):-1]
    if len(txt) >= 3:
        center = txt[len(txt)//2]
else:
    last_half = txt[:(len(txt)//2)-1:-1]

print(f"{first_half}{center}{last_half}")
