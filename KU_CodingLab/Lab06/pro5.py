input_num = 0
max = 0
able_to_see = 0

while input_num != -1:
    input_num = int(input())
    if (input_num > max):
        max = input_num
        able_to_see += 1

print(able_to_see)
