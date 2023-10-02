'''

'''
'''
def space_checking(cu_str, str_lst, idx):
    #if idx == 0:
        #return cu_str == " " and str_lst[idx+1].isalpha()        
    if idx != len(str_lst) - 1:
        return cu_str == " " and not (str_lst[idx-1].isalpha() and str_lst[idx+1].isalpha())   
    return False

input_strs = input()

txt = ""
new_str = ""
for i in range(len(input_strs)):
    cu_str = input_strs[i]
    if (cu_str == "," or i == len(input_strs) - 1):
        if txt == " " or cu_str == " ":
            txt,cu_str = "", ""
        
            
        new_str += f'"{txt}"' + "," if  i != len(input_strs) - 1 else f'"{txt + cu_str}"'
        txt = ""
        continue
    elif space_checking(cu_str, input_strs, i):
        continue
    #elif i == len(input_strs) - 1:
        #new_str += f'"{cu_str}"' if (cu_str != " ") else '""'
    
    txt += cu_str
    
print(new_str)
'''

'''
input_lst = input().split(",")
#print(input_lst)

txt=""
for i in range(len(input_lst)):
    now_el = input_lst[i]
    print(f'"{now_el.strip()}"', end=",") if i != len(input_lst) - 1 else print(f'"{now_el.strip()}"')
'''   
