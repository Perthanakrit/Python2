def toUpper(m_str, idx, symbols):
    if (m_str[idx-1] in symbols):
        return m_str[idx].upper()
    return m_str[idx]


input_str = input()
symbol = "-_=.$"

camelCase = ""
for i in range(len(input_str)):
    current_ch = input_str[i]
    if i == 0:
        camelCase += current_ch.lower()
        continue
    elif current_ch in symbol:
        continue
    camelCase += toUpper(input_str, i, symbol)
  
print(camelCase)