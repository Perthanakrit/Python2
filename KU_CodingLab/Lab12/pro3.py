'''
origin: [['a', ' = ', 'equations of time'], 
         ['integer', ' = ', '365'], 
         ['b', ' = ', 'c']]
'''
import math

def split_one_equal(mstr):
    lst = []
    find_equal = False
    txt = ""
    for m in mstr:
        if (not find_equal and m == "="):
            find_equal = True
            lst.append(txt.strip())
            lst.append(" = ")
            txt = ""
            continue
        
        txt += m
    
    lst.append(txt.strip())
    return lst


def find_max_len(lst, idx):
    max_len = -math.inf
    for el in lst:
        if (len(el[0]) > max_len ):
            max_len = len(el[0])
    
    return max_len - len(lst[idx][0]) if len(lst[idx][0]) < max_len else 0


str_lst = []

while True:
    input_str = input()
    #print(input_str)
    if (input_str == "-1"): break
    #print(split_one_equal(input_str))
    str_lst.append(split_one_equal(input_str))

#print("origin:",str_lst)


for i in range(len(str_lst)):
    txt = ""
    if (i == 0):
        space = " " * (find_max_len(str_lst, i))
        str_lst[i][0] = space + str_lst[i][0]
        continue
    
   
    if  len(str_lst[i][0]) < len(str_lst[0][0]):
        space = " " * (len(str_lst[0][0]) - len(str_lst[i][0])) if str_lst[i][0] != "" else " " * len(str_lst[0][0])
        
        str_lst[i][0] = space + str_lst[i][0]
        
#print("modify:",str_lst)

for sup_lst in str_lst:
    for el_str in sup_lst:
        print(el_str, end="")
    print()