def isvowel(char):
    if (char == "A" or char == "E" or char == "I" or char == "O" or char == "U"):
        return True
    return False

input_str = str(input())

no_vowel_lst = []

for s in input_str:
    if (isvowel(s.upper()) == False):
        no_vowel_lst.append(s)
txt = ''

for c in no_vowel_lst:
    txt += c

print(txt)
