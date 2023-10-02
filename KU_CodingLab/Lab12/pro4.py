def split_filename_type(txt:str):
    is_file_name = False
    lst = []
    result = ""
    
    for i in range(len(txt)-1, -1, -1):
        if is_file_name == False:
            if (txt[i] == "."):
                lst.append(result)
                result = ""
                is_file_name = True
                continue      
        
        result = txt[i] + result
         
    lst.append(result)
    lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0]
    
    return lst
        

def filename_validation(name:list): 
    name[0] = name[0][:15]
    if ( len(name) > 1):
        name[1] = name[1][:3]
        
    return name


fobidden_sym = ['\\',"/","*",":", "|",'"',"<",">",".", " "]

input_str = input()

filename = filename_validation(split_filename_type(input_str))

for sym in fobidden_sym:
    filename[0] = filename[0].replace(sym, "_")
    if len(filename) > 1:
        filename[1] = filename[1].replace(sym, "_")
    
for i in range(len(filename)):
    print(filename[i], end=".") if i != len(filename) - 1 else print(filename[i])
        

