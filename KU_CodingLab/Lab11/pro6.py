'''
paper -> pappeper
papapripikap

apa -> a
ipi -> i
ap -> a
'''

def font_back_vowel(lst, idx, vowels):
    if (lst[idx] == "p" and idx == len(lst) - 1):
        return True  
    return lst[idx] == "p" and (lst[idx-1] in vowels  and lst[idx+1] in vowels and lst[idx-1] == lst[idx+1] or lst[idx-1] in vowels)

def validate_input(str_input):
    for s in str_input:
        if (s.isalpha() == False and s != " ") or len(str_input) > 100:
            return False
        if (str_input[0].isalpha() == False or str_input[len(str_input)- 1].isalpha() == False or len(str_input) > 100):
            return False
    return True
       
def decode(lst, idx, vowels):
    if idx < len(lst) - 2 :
        if (f"{lst[idx]}{lst[idx+1]}{lst[idx+2]}" == f"{lst[idx]}p{lst[idx]}"):
            return 2
    elif idx < len(lst) - 1 and idx >= len(lst) - 2:
        if (f"{lst[idx]}{lst[idx+1]}" == f"{lst[idx]}p"):
            return 1       
    return 0

input_word = input().lower()
skip = 0
if (validate_input(input_word)):
    vowels = ["a", "e", "i", "o", "u"]
    
    txt = ""
    for i in range(len(input_word)): 
        if input_word[i] in vowels and skip <= 0:
            txt += input_word[i]
            skip = decode(input_word, i, vowels)
            continue
        if skip <= 0:
            txt += input_word[i]
        skip -= 1
        
    print(txt)
   