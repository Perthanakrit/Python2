equation_ls = []
while True:
    x = input()
    if (x == "-1"):
        break
    equation_ls.append(x)

print(equation_ls)

left_ls = [] 
right_ls = []

for eq in equation_ls:
    part_ls = eq.partition("=")
    print(part_ls)
    left_ls.append(part_ls[0].strip())
    right_ls.append(part_ls[2].strip())

print(left_ls)
print(right_ls)

len_left_ls = [len(i) for i in left_ls]

max_len = max(len_left_ls)

for i in range(len(equation_ls)):        
    print(f"{left_ls[i].rjust(max_len)}" + " = " + f"{right_ls[i]:<}")
