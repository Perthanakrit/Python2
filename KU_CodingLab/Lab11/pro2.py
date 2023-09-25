def isvowel(char):
    if (char == "A" or char == "E" or char == "I" or char == "O" or char == "U"):
        return True
    return False

input_str = str(input())
count = 0
for s in input_str:
    if (isvowel(s.upper())):
        count += 1
        
print(count)
