def new_order(num_lst):
    new_numbers = []
    max_num = 0
    for num in num_lst:
        if num >= max_num:
            max_num = num
            new_numbers.append(max_num)
        
    return new_numbers

numbers = []

while True:
    input_num = int(input())
    if (input_num == -1):
        break
    numbers.append(input_num)

print(new_order(numbers))