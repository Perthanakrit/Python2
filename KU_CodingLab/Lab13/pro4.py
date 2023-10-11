'''
Sun  Mom Tue Meb Thu Fri Sat
1
8    9   10  
15   16  17   18  19  20  21
22
29   30  31   1   2   3   4
5(36)
'''
'''
Sun  Mom Tue Meb Thu Fri Sat
              1   2   3   4
5
12 
19   
26   27  28 29   30  31   1
-------
2(33)
9
16
23  24    25 26  27 28   1
---
2(30)


20-01   31-01
02-02   01-01
False    True
'''

def invalid(start_d,end_d):
    err_count = 0
    if not (0 < start_d[1] <= 12) or  not (0 < end_d[1] <= 12):
        err_count += 1
        print("Wrong Month")
    if not (0 < start_d[0] <= 31) or  not (0 < end_d[0] <= 31):
        err_count += 1
        print("Wrong Day")    
    return err_count >= 1

def create_date(first:int,origin:int ,limit:int):
    ls = []
    current_sun = first
    
    while current_sun <= limit:
        if first <= current_sun <= limit:
            ls.append(current_sun)
        current_sun += 7
    return ls


def sunday_each_month(first_sun, start, end):
    month = 1
    sunday_lst = []
    
    start_date,start_month = int(start[0]), int(start[1])
    end_date, end_month = int(end[0]) if int(end[1]) == month else 31, int(end[1])
    
    if start_date > end_date and start_month <= end_month: 
        end_date,start_date = start_date, end_date
        
    sunday_lst.extend(create_date(first_sun, start_date, end_date))
    month += 1
    
    #first_sun    
    while month <= end_month:
        first_sun = sunday_lst[len(sunday_lst) - 1] + 7
        if month != 2 and month in thirty_days: # ยน
            first_sun -= 31
            end_date = int(end[0]) if int(end[1]) == month else 30
        elif month in thirty_one_days: # คม
            first_sun -= (30 if month - 1 != 2 else 28) 
            end_date = int(end[0]) if int(end[1]) == month else 31
        elif month == 2:
            first_sun-= 31
            end_date = int(end[0]) if int(end[1]) == month else 28
            
        sunday_lst.extend(create_date(first_sun, first_sun, end_date))
        month += 1
                 
    return sunday_lst


thirty_one_days = [1,3,5,7,8,10,12]
thirty_days = [4,6,9,11]

start_date = [ int(st) for st in input().split("-")]
end_date = [ int(st) for st in input().split("-")]
first_sun_of_month = int(input())

if not invalid(start_date, end_date):
    print(sunday_each_month(first_sun_of_month, start_date, end_date))