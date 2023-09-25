input_num = int(input())
num_of_space = input_num - 1

for i in range(input_num):
    start = (2 * i + 1) * "*"
    space = " " * num_of_space
    print(f"|{space}{start}{space}|")
    num_of_space -= 1


