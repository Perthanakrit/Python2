# print((8+1+8+1+8+1) % 9)
# print(818282 % 9)
# print(8+1+8+1+8+1)
'''
    num % != 0 => print(เศษ)
'''
num_input = int(input())

count = 0
u_num = num_input
while u_num != 0:
    u_num //= 10
    count += 1

index = count - 1

summ = 0

if (num_input % 9 == 0):
    while True:
        num = num_input // (10 ** index)
        num_input -= num * (10 ** index)
        index -= 1
        summ += num

        if (index < 0):
            break
    print("Yes", summ)
else:
    print("No", num_input % 9)
