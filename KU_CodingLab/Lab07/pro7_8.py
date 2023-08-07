day_target = input()
day_target = day_target.capitalize()
n = int(input())

date = 1
day = ""
week = 0

able_to_run = day_target == "Sunday" or day_target == "Monday" or day_target == "Tuesday" or day_target == "Wednesday" or day_target == "Thursday" or day_target == "Friday" or day_target == "Saturday"

if (able_to_run and (n >= 1 and n <= 31)):
    day = day_target
    while date < n:
        if (day == "Monday"):
            date += 1
            day = "Tuesday"
        elif (day == "Tuesday"):
            date += 1
            day = "Wednesday"
        elif (day == "Wednesday"):
            date += 1
            day = "Thursday"
        elif (day == "Thursday"):
            date += 1
            day = "Friday"
        elif (day == "Friday"):
            date += 1
            day = "Saturday"
        elif (day == "Saturday"):
            date += 1
            day = "Sunday"
        elif (day == "Sunday"):
            date += 1
            day = "Monday"

    print(day)

else:
    print("ERROR")
