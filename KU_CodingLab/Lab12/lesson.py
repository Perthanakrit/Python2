# String Functions

# 1) len
'''
import math 
max_len_str = -math.inf
max_str = ""

while True: 
    input_str = input()
    if (input_str == ""):
        break 
    if (len(input_str) > max_len_str):
        max_len_str = len(input_str)
        max_str = input_str
        
print(max_str)
'''

# 2) ord(char) and chr(number)
'''
ch_input = input()
n = int(input())

result_ascii_ch = ord(ch_input) + n

print(chr(result_ascii_ch))
'''

# 3) max(string) and min(string)
'''
result_txt = ""
count = 1
while True:
    input_str = input()
    if (input_str == ""):
        break
    
    if (count % 2 != 0):
        result_txt += max(input_str)
    else:
        result_txt += min(input_str)

    count += 1
    
print(result_txt)
'''

# 3) lowercase and UPPERCASE
'''
input_str = input()
new_str = ""

for ch in input_str:
    if ch.islower():
        new_str += ch.upper()
    elif ch.isupper():
        new_str += ch.lower()
    else:
        new_str += ch
print(new_str)
'''

# 4) other methods

input_str = input()
sub1 = input()
sub2 = input()

print(input_str.find(sub1))
print(input_str.count(sub1))
print(input_str.replace(sub1, sub2))