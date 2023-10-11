def extract_string(text):
    newlst = []
    txt = ""
    for i in range(len(text)):
        txt += text[i]
        if text[i].isdigit():
            if i == len(text) - 1:
                newlst.append(int(txt))
                txt = ""
                continue
            if not text[i+1].isdigit():
                newlst.append(int(txt))
                txt = ""
            continue        
        
        if i != len(text) -1:
            if text[i+1].isdigit():
                newlst.append(txt)
                txt = ""
        else: 
            newlst.append(txt)
            txt = ""            
   
    return newlst
    

print( extract_string("G2X3t4") )
print( extract_string("AB12XY23"))
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )

