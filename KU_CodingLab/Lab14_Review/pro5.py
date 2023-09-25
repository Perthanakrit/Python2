'''
''
a < b
b < d
d < e
e < s
... s < t
'''

def input_to_lst(txt):
    txt_split = []
    for w in txt:
        txt_split.append(w)
    
    txt_split.append('')
    return txt_split


input_txt = input()

if (input_txt.isalpha()):
    word_lst = input_to_lst(input_txt)
    
    for i in range(len(word_lst) - 1):
        if (word_lst[i+1] < word_lst[i] or word_lst[i+1] == ''):
            print(i+1)
            break
else:
    print(0)