# for x in [4,6,3,10,5] : print( x if x % 2 == 0 )

def invalid(start_d, end_d, first_sun):
    err_count = 0
    wrong_day_31 = (start_d[0] > 31 and start_d[1] in thirty_one_days) or (
        end_d[0] > 31 and end_d[1] in thirty_one_days)
    wrong_day_30 = (start_d[0] > 30 and start_d[1] in thirty_days) or (
        end_d[0] > 30 and end_d[1] in thirty_days)
    wrong_day_28 = (start_d[0] > 28 and start_d[1] == 2) or (
        end_d[0] > 28 and end_d[1] == 2)
    wrong_first_sun = first_sun < 1 or first_sun > 31

    if not (0 < start_d[1] <= 12) or not (0 < end_d[1] <= 12):
        err_count += 1
        print("Wrong Month")
    if wrong_day_31 or wrong_day_30 or wrong_day_28 or wrong_first_sun:
        err_count += 1
        print("Wrong Day")
    return err_count >= 1


def create_sunday(first: int, last_day: int, last_month: int):
    ls = []
    current_sun = first

    while current_sun <= last_day:
        ls.append(current_sun)
        current_sun += 7

    # if len(ls) < 1:
    #     ls.append(current_sun - 7)

    return ls


def sunday_on_lst(first_day, start, end):
    sunday_lst = []

    for i in range(1, end[1] + 1):
        # last_day_month = 0
        if i in thirty_one_days:
            if i != 1:
                if i - 1 == 2:
                    first_day -= 28
                elif i - 1 >= 2:
                    first_day -= 30
            last_day_month = 31
        elif i in thirty_days:
            first_day -= 31
            last_day_month = 30
        elif i == 2:
            first_day -= 31
            last_day_month = 28

        # first sunday, last day input
        sunday_lst.append(create_sunday(first_day, last_day_month, i))

        previous = sunday_lst[len(sunday_lst) - 1]
        first_day = previous[len(previous) - 1] + 7

    # print(sunday_lst)
    return sunday_lst


thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
thirty_days = [4, 6, 9, 11]

run = True
start_date = [st for st in input().split("-")]
if not (start_date[0].isdigit() and start_date[0].isdigit()):
    run = False
else:
    start_date[0] = int(start_date[0])
    start_date[1] = int(start_date[1])

end_date = [st for st in input().split("-")]
if not (end_date[0].isdigit() and end_date[0].isdigit()):
    run = False
else:
    end_date[0] = int(end_date[0])
    end_date[1] = int(end_date[1])

n = int(input())

if run:
    if not invalid(start_date, end_date, n):
        count = 0
        if start_date[0] >= end_date[0] and start_date[1] >= end_date[1]:
            end_date[0], start_date[0] = start_date[0], end_date[0]
            end_date[1], start_date[1] = start_date[1], end_date[1]

        m_lst = sunday_on_lst(n, start_date, end_date)
        for m in range(start_date[1]-1, end_date[1]):
            for d in m_lst[m]:
                if start_date[1]-1 < m < end_date[1]-1:
                    count += 1
                    # print(d)
                elif m == end_date[1]-1:
                    if d <= end_date[0]:
                        count += 1
                elif m == start_date[1]-1:
                    if start_date[0] <= d:
                        count += 1

        print(count)
