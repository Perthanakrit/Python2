def remove_duplicates(t):
    if (len(t) == 0):
        return 
    new_lst = []
    
    new_lst.append(t[0])
    current_el = t[0]
    
    for el in t:
        count = 0
        for new_el in new_lst:        
            if (new_el != el):
                count += 1
            if (count >= len(new_lst)):
                new_lst.append(el)

    return new_lst

my_lst =[]
print(remove_duplicates(my_lst))
