'''
236  
6 = 236 // 10^ 1 % 10
3 = 236 // 10 % 10
2 = 236 // 100 % 10
'''

num = int(input())
count = 0
u_num = num

if (num <= 0):
    print("ERROR")
else:
    while u_num != 0:
        u_num //= 10
        count += 1

    index = 0

    while index <= count - 1:
        cur_num = (num // (10 ** index)) % 10
        print(cur_num)
        index += 1
# if (num > 0):
#     while index >= 0:
#         print(int(num_str[index]))
#         index -= 1
# else:
#     print("ERROR")
