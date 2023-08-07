x = int(input())
n = int(input())

week = 0
date = x
day = ""

if (x >= 1 and x <= 7) and (n >= 1 and n <= 31):
    while True:
        if (7 * week) + x == n:
            day = "Sunday"
        elif (7 * week) + (x + 1) == n or (7 * week) + (x - 6) == n:
            day = "Monday"
        elif (7 * week) + (x + 2) == n or (7 * week) + (x - 5) == n:
            day = "Tuesday"
        elif (7 * week) + (x + 3) == n or (7 * week) + (x - 4) == n:
            day = "Wednesday"
        elif (7 * week) + (x + 4) == n or (7 * week) + (x - 3) == n:
            day = "Thursday"

        elif (7 * week) + (x + 5) == n or (7 * week) + (x - 2) == n:
            day = "Friday"

        elif (7 * week) + (x + 6) == n or (7 * week) + (x - 1) == n:
            day = "Saturday"

        if day != "":
            print(day)
            break

        week += 1


else:
    print("ERROR")
