input_num = int(input())
result = 1

while input_num > 0:
    num = input_num % 10
    input_num //= 10
    if (num % 2 == 0):
        result *= num

if (result == 1):
    result = -1

print(result)
