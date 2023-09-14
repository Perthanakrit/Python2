#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#total = 0
#for num in primes:
#    total += num

#print(total)


import math

def find_max(list):
    max_num = -math.inf
    
    for num in list:
        if (num > max_num):
            max_num = num
    return max_num
    

print(find_max([1, 2, 3, 4]))
print(find_max([4, 3, 2, 1]))
print(find_max([4, 3, 5, 9, 7, 2, 4, 4, 10, 0, 11, 8]))
print(find_max([-7, -9, -8, -2, -7, -11, -4, -5]))