num_ls_input = []
while True:
    n = int(input())
    if n == 0:
        break
    num_ls_input.append(n)

max_equal = 0
# print(num_ls_input)
for i in range(len(num_ls_input)):
    curr_equl = 0
    for j in range(i, len(num_ls_input)):
        curr_equl += num_ls_input[j]
        # print(curr_equl)
        if max_equal < curr_equl:
            max_equal = curr_equl

print(max_equal)
