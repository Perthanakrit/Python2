def toUpper(m_str, idx, symbols):
    if idx > 1:
        if (m_str[idx-1] in symbols and m_str[idx].islower()):
            return m_str[idx].upper()
    return m_str[idx]


input_str = input()
symbol = ["-","_","=",".","$"]
isSymbol = False
camelCase = ""
for i in range(len(input_str)):
    current_ch = input_str[i]
    if i == 0:
        if current_ch not in symbol:
            camelCase += current_ch.lower()
    else:
        if current_ch not in symbol:
            if isSymbol:
                camelCase += current_ch.upper()
                isSymbol = False
            else:
                camelCase += current_ch.lower()
        else:
            isSymbol = True
    
print(camelCase)

'''
-a_b=c.d$d
A-very.long$name
h_lveRT.Long=na.jpg
'''