'''
papapripikap
'''

def font_back_vowel(lst):
    return input_word[i] == "p" and (input_word[i-1] in vowel  and input_word[i+1] in vowel and input_word[i-1] == input_word[i+1] or input_word[i-1] in vowel or input_word[i-2] in vowel)

def validate_input(str_input):
    for s in str_input:
        if (s.isalpha() == False and s != " ") or len(str_input) > 100:
            return False
        if (str_input[0].isalpha() == False or str_input[len(str_input)- 1].isalpha() == False or len(str_input) > 100):
            return False
    return True
    

def skip_to_decode(lst, idx, vowels):
    if (lst[idx:idx+3] == f"{lst[idx]}p{lst[idx]}"):
        return True
    elif (lst[idx:idx+2] == f"{lst[idx]}p"):
        return True
    return False
    

input_word = input().lower()

if (validate_input(input_word)):
    vowel = ["a", "e", "i", "o", "u"]    
    txt = ""
    skip = 1
    input_word = " " + input_word + " "
    
    for i in range(len(input_word)): 
        if (i != 0 and i != len(input_word)-1):
            if (skip <= 0):
                txt += input_word[i]
        
            if (input_word[i] in vowel and skip <= 0):   
                skip = skip_to_decode(input_word, i, vowel)
            
    print(txt)
