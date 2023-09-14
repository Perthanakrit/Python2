def accum_sum(og_nums):
    new_nums = []
    sum_num = 0
    
    for num in og_nums:
        sum_num += num
        print(sum_num)
    
original_numbers = []

while True:
    input_num = int(input("Enter a number (0 to end): "))
    if (input_num == 0):
        print("Original list: ")
        print(original_numbers)
        print("Accumulative Sum:")
        accum_sum(original_numbers)
        break
    if (input_num > 999 or input_num < 0):
        print("Number is out of range.")
        continue
    
    original_numbers.append(input_num)
    

        
