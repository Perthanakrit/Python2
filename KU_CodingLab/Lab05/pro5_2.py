import math

hours = int(input("Enter number of hours: "))
mins = int(input("Enter number of minutes: "))

total_amount = 0

if (hours < 0 or (mins < 0 or mins == 60)):
    print("Input Error!")
else:
    if (mins <= 15 and hours == 0):
        print("No charge, thanks.")
    else:
        hours += (math.ceil(mins / 60))
        total_amount = 10
        if (hours >= 3):
            total_amount += ((hours - 3) * 10 + 10)

        print(f"Total amount due is {total_amount} Bahts.")
