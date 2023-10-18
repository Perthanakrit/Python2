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
20-02
10-10
44
'''


def invalid(start_d, end_d, first_sun):
    err_count = 0
    # print(start_d, end_d, first_sun)
    wrong_first_sun = first_sun < 1 or first_sun > 31
    wrong_day_start, wrong_day_end = False, False

    if not (0 < start_d[1] <= 12) or not (0 < end_d[1] <= 12):
        err_count += 1
        print("Wrong Month")

    if (0 < start_d[1] <= 12):
        wrong_day_start = start_d[0] > days_in_month[start_d[1]]

    if (0 < end_d[1] <= 12):
        wrong_day_end = end_d[0] > days_in_month[end_d[1]]

    if wrong_day_start or wrong_day_end or wrong_first_sun:
        err_count += 1
        print("Wrong Day")
    return err_count >= 1


days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_date = [int(st) for st in input().split("-")]
end_date = [int(st) for st in input().split("-")]
first_sun_of_month = int(input())

if start_date[0] >= end_date[0] and start_date[1] >= end_date[1]:
    end_date[0], start_date[0] = start_date[0], end_date[0]
    end_date[1], start_date[1] = start_date[1], end_date[1]

if not invalid(start_date, end_date, first_sun_of_month):
    start, end = 0, 0
    for i in range(1, end_date[1]+1):
        if i <= start_date[1]:
            if i == start_date[1]:
                start += start_date[0]
            else:
                start += days_in_month[i]

        if i == end_date[1]:
            end += end_date[0]
            # print(i, start, end)
        else:
            end += days_in_month[i]

    sunday = first_sun_of_month
    count = 0

    for d in range(first_sun_of_month,  end+1):
        if start <= sunday <= end:
            # print(sunday, end=" ")
            count += 1
        sunday += 7
    # print()
    print(count)
