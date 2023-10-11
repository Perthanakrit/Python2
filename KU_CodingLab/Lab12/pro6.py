def number_varidation(nums:list):
    num = 0
    # integer
    if not nums[0][0].isdigit():
        return "ERROR"
    
    last = nums[0][len(nums[0])-1]
    if len(nums[0]) > 1:
        for el in nums[0]:
            if (len(el) > 3) or len(last) != 3  or not el.isdigit():
                    return "ERROR"  
    
    num = int("".join(nums[0])) 
    
    # float
    if len(nums) > 1:
        if not nums[1].isdigit() or len(nums[1]) > 2:
            return "ERROR"
        num += float(int(nums[1]) / 100)
    
    return num + 1

num_input = input()
ls = num_input.split(".")
if len(ls) > 2:
    print("ERROR")
else:
    ls[0] = ls[0].split(",")
    print(number_varidation(ls))



