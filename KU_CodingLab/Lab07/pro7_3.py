#print("{:n}".format(1323.343))
#print("{:.1s}".format('hello'))
#print(F"{1+2}")

num_day = int(input())
hr = int(input())
mins = int(input())

time = ""
day = ""

your_time = hr + (mins/100)

if (4.01 <= your_time <= 12.00 ):
    time = "morning"
elif (12.01 <= your_time <= 18.00 ):
    time = "afternoon"
elif (18.01 <= your_time <= 22.00):
    time = "evening"
elif (your_time <= 4.00 or your_time >= 22.01):
    time = "night"


if (num_day == 1):
    day = "sunday"
elif (num_day == 2):
    day = "monday"
elif (num_day == 3):
    day = "tuesday"
elif (num_day == 4):
    day = "wednesday"
elif (num_day == 5):
    day = "thursday"
elif (num_day == 6):
    day = "friday"
elif (num_day == 7):
    day = "saturday"

IMG_FILE = f"good-{time}-{day}.png"

print(IMG_FILE)

