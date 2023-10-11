# List Methonds

'''
1. Add List
- append 
- extend
- insert(index, data)


        
# List Comprhension
#fruits = ["appel", "banana", "kiwi"]
#filtered = [x for x in fruits if "a" in x]
#print(filtered)

numbers = list(range(100))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)        
'''
'''
def create_factors_3_7(n):
    new_lst = []
    for el in n:
        if (el > 0):
            if (el % 3 == 0 or el % 7 == 0):
                new_lst.append(el)
        
    
    len_lst = len(new_lst)
    swapped = False
    for i in range(len_lst-1):
        for j in range(len_lst-i-2, -1, -1):
            if (new_lst[j] > new_lst[j+1]): 
                swapped = True
                new_lst[j], new_lst[j+1] =  new_lst[j+1], new_lst[j]
            
        if (not swapped):
            return new_lst 
        
    return new_lst

ls = []

while True:
    input_el = int(input())
    if (input_el == 0):
        break
    ls.append(input_el)
    
print(create_factors_3_7(ls))
'''

'''
-pop
-remove
'''
#def create_factors_3_7(ls):
    #count = 0
    #while len(ls) > count:
        #item = ls.pop()
        #if item % 3 == 0 or item % 7:
            #count += 1
        
    #return count
'''
def create_factors_3_7(ls):
    count = 0
    new_ls = [[],[]]
    while len(ls) > 0:
        item = ls.pop()
        if item % 3 == 0 or item % 7 == 0:
            new_ls[0].append(item)
        else:
            new_ls[1].append(item)
        
    return new_ls

m_ls = []
while True:
    input_el = int(input()) 
    if (input_el == 0):
        break
    m_ls.append(input_el)
    
print(create_factors_3_7(m_ls))
'''

# List: sort,sort(reverse=True), reverse
'''
def filter_sort_factors_3_7(n):
    new_lst = [[],[]]
    for el in n:
        if (el > 0):
            if (el % 3 == 0 or el % 7 == 0):
                new_lst[0].append(el)
            else:
                new_lst[1].append(el)
    new_lst[0].sort()
    new_lst[1].sort(reverse=True)
    return new_lst


input_lst = [5,9,1,6,2,10,7,21]
print(filter_sort_factors_3_7(input_lst))
'''                

# count(data) index(data)
                
# split(delimeter)
'''
ls = int(input())
print(ls.split("."))

point1 = input().split(",")
point2 = input().split(",")

x_value = float(point1[0]) + float(point2[0])
y_value = float(point1[1]) + float(point2[1])

print(f"{x_value:.1f},{y_value:.1f}")
'''

# List to String : list.join()
ls = []
while True:
    input_str = input()
    if input_str == "":
        break
    ls.append(input_str)
    
print("".join(ls))
    