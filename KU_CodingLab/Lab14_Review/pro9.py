my_dict = {}

n = int(input())

for i in range(n):
    alpha_ch = input()
    if alpha_ch not in my_dict:
        my_dict[alpha_ch] = 1
    else:
        my_dict[alpha_ch] += 1

is_empty = True
for k in my_dict:
    if my_dict[k] >= (n//2 + 1):
        is_empty = False
        print(k)
if is_empty:
    print(0)
