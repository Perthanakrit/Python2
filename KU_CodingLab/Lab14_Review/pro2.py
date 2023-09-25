'''
tiger -> tig
         +
lion -> on
     =  tigon
     
lion +  butterfly : 0.30994415283203125
'''
import time


def f_name(name, vowels):
    txt = ""
    found_vowel = 0
    
    for i in range(len(name)):
        if name[i] in vowels:
            found_vowel += 1
            if (found_vowel == 2):
                return txt
        txt += name[i]
        
    return name


def m_name(name, vowels):
    txt = ""
    found_vowel = 0
    
    for i in range(len(name)):   
        if (found_vowel >= 1):
            txt += name[i]
            continue
        if name[i] in vowels:
            found_vowel += 1    
              
    return name if (txt == "") else txt


f_breeder = input()
m_breeder = input()
vowel_lst = ["a", "e", "i", "o", "u"]

#start = time.time()
print(f_name(f_breeder, vowel_lst) + m_name(m_breeder, vowel_lst))
#end = time.time()

#print((end-start) * 1000)

