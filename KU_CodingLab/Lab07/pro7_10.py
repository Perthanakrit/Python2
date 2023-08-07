input_num = int(input())

summ = 0
while input_num > 0:
    num = (input_num % 10)
    input_num //= 10
    if (num % 2 != 0):
        summ += num

if (summ > 0):
    print(summ)
else:
    print("-1")
