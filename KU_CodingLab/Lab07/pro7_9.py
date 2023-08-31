'''
20 => (1, 20) (2, 10) (4,5)

'''

input_num = int(input())

j =  input_num
a, b = 1, input_num

result = input_num + a

while a < b:
    i = b
    while True:
        if (a * i == input_num):
            b = i
            summ = a + b
            break
        if (i <= 0):
            break
        i -= 1   
    a += 1
    if (summ < result):
        result = summ

print(result)
    
    