def toUpper(m_str, idx, symbols):
    if idx > 1:
        if (m_str[idx-1] in symbols and m_str[idx].islower()):
            return m_str[idx].upper()
    return m_str[idx]


input_str = input()
symbol = "-_=.$"

camelCase = ""
for i in range(len(input_str)):
    current_ch = input_str[i]
    #if i == 0 and current_ch not in symbol:
        #camelCase += current_ch.lower()
        #continue
    if current_ch in symbol:
        continue
    if current_ch.isalpha() or current_ch.isdigit():
        camelCase += toUpper(input_str, i, symbol)
    
    if len(camelCase) <= 1 :
        if current_ch not in symbol:
            camelCase = camelCase.lower()
    
print(camelCase)

'''
-a_b=c.d$d
A-very.long$name
h_lveRT.Long=na.jpg
'''