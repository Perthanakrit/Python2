target_num = int(input())
count = 0
while target_num != 0:
    target_num //= 10
    count += 1

print(count)
