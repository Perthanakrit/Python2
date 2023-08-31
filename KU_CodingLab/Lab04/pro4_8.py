mins_due = int(input("Minutes before due: "))
if (mins_due < 0):
    mins_due *= -1

tempe = float(input("Temperature: "))

raining = input("Is it raining (y/n)? ")

done = "do"

days = (mins_due + 59) / 60 / 24

if (days > 5):
    done = "not do"
elif (days < 2):
    if (tempe > 40 or (tempe > 25 and (raining == "Y" or raining == "y"))):
        done = "not do"
    elif (tempe <= 40 or (tempe <= 25 and (raining == "N" or raining == "n"))):
        done = "do"
else:
    if (tempe > 40 or (tempe > 25 and raining == "Y")):
        done = "not do"
    elif (tempe <= 40 or (tempe <= 25 and raining == "N")):
        done = "do"


print(f">>> {int(days):d} days before due.")
print(f">>> I will {done} the assignment.")
