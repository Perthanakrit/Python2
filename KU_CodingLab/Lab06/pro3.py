import time

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

first_input = first_num
second_input = second_num

n1, n2 = 0, 0

if (first_num > second_num):
    n1 = first_num
    n2 = second_num
else:
    n1 = second_num
    n2 = first_num

while True:
    mod = n1 % n2
    n1 = n2
    n2 = mod
    
    if (mod <= 0):
        break

while True:
    first_num //= n1
    second_num //= n1
    #print(first_num, second_num)
    case_n1 = (first_num % n1 == 0 and second_num % n1 == 0) and n1 == 1
    if (first_num % n1 != 0 or second_num % n1 != 0 or case_n1):
        break

lcm = (first_num * second_num) * n1


print("  >> gcd({0}, {1}) ={2:>7}".format(first_input, second_input, n1))
print("  >> lcm({0}, {1}) ={2:>7} ".format(first_input, second_input, lcm))


'''
20 % 8 = 4 
8 % 4 = 0

135 % 1
'''