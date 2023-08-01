'''
< 2 day left -> send
> 5 days left -> unsend
temp > 40 or temp > 25 and rainning -> unsend
'''

mins_due = int(input("Minutes before due: "))
if (mins_due < 0):
    mins_due *= -1

tempe = float(input("Temperature: "))

raining = input("Is it raining (y/n)? ")
raining = raining.capitalize()

done = "do"

days = mins_due / 60 / 24

if (days - int(days) >= 0.5):
    days = int(days) + 1
else:
    days = int(days)

if (days > 5):
    done = "not do"
elif (days < 2):
    if (tempe > 40.0 or (tempe > 25.0 and raining == "Y")):
        done = "not do"
    elif (tempe <= 40.0 or (tempe <= 25.0 and raining == "N")):
        done = "do"
elif (days >= 2 and days <= 5):
    if (tempe > 40.0):
        if (tempe > 25.0 and raining == "Y"):
            done = "not do"
        elif (tempe <= 25.0 and raining == "N"):
            done = "do"
    elif (tempe <= 40.0 or (tempe <= 25.0 and raining == "N")):
        done = "do"


print(f">>> {days} days before due.")
print(f">>> I will {done} the assignment.")
