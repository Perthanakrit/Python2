def input_validation(input_value):
    for v in input_value:
        if (v.isalpha()):
            return True 
        
    return len(input_value) > 3 or input_value == ""


def int_to_eng(value, num, num_dict): 
    txt = ""
    if ( value >= 100):
        value //= num
        txt = f"{num_dict[value]}-{num_dict[num]}"
    elif (20<= value < 100):
        value //= num
        value *= 10
        txt = num_dict[value]
    elif (11<= value < 20):
        txt = num_dict[value]
    else:
        txt = num_dict[value]
    
    return txt


num_dict = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",8:"eight", 9:"nine", 10:"ten",11:"eleven",
 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19: "nineteen",
 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 
 100: "hundred"
}
        
input_num = input()

if (input_validation(input_num)):
    print("ERROR")
else:
    eng_number = []
    
    int_num = int(input_num)
    
    i = len(input_num) 
    while i > 0:
        i -= 1
        digit  = int_num // 10 ** i    
        value_num = (10 ** i) * digit
    
        if (digit > 0 and value_num >= 10 ** i ):
            eng_number.append(int_to_eng(int_num,10 ** i, num_dict))
        
        int_num -= int_num if (11<=int_num <= 19) else value_num
       
    print('-'.join(eng_number))