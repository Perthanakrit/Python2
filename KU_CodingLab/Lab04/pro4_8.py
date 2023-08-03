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
# raining = raining.capitalize()

done = "do"

days = mins_due / 60 / 24

if (days - int(days) >= 0.5):
    days = int(days) + 1
else:
    days = int(days)

if (days > 5):
    done = "not do"
elif (days < 2):
    if (tempe > 40 or (tempe > 25 and (raining == "Y" or raining == "y"))):
        done = "not do"
    elif (tempe <= 40 or (tempe <= 25 and (raining == "N" or raining == "n"))):
        done = "do"
elif (days >= 2 and days <= 5):
    if (tempe > 40 or (tempe > 25 and (raining == "Y" or raining == "y"))):
        done = "not do"
    elif (tempe <= 40 or (tempe <= 25 and (raining == "N" or raining == "n"))):
        done = "do"


print(f">>> {days} days before due.")
print(f">>> I will {done} the assignment.")
