def summ_fibonacci(n:int, type_of:str):
    if not (type_of == "e" or type_of == "o"):
        return "ERROR"    
    a1,a2 = 0, 1
    summ = 0
    result = 0 
    
    for i in range(n+1):
        summ = a1 + a2
        a2, a1 = a1,  summ
        if type_of == "e" and i % 2 == 0:
            result += summ
        elif type_of == "o" and i % 2 != 0:
            result += summ 
                 
    return result if result > 0 else "ERROR"

    
n = int(input())
type_of_num = input().lower()
if n >= 0:
    print(summ_fibonacci(n, type_of_num))
else:
    print("ERROR")