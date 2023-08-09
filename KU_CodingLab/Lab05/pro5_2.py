'''
120 -> free
180 -> +20
240 -> +20
300 -> +50

* totalPrice 300 - 3000 => park 3 and 4 hr Free
* totalPrice least 3001 => Free park service
'''


hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))

# if (hours < 0):
#     hours *= -1

# if (minutes < 0):
#     minutes *= -1

# if (buyAmt < 0):
#     buyAmt *= -1

fee = 0

over_min = hours == 20 and minutes >= 1

if (hours < 0 or hours > 20 or minutes < 0 or minutes > 59 or over_min):
    print("Invalid time.")

else:
    hours += (1 if (minutes % 60) > 0 else 0)
    total_hr = hours

    while (True):
        if (buyAmt < 3001 and total_hr >= 3):

            if (total_hr >= 3 and total_hr <= 4):
                fee += 0 if (buyAmt >= 300) else 20
                total_hr -= 1
            elif (total_hr >= 5):
                fee += 50
                total_hr -= 1
            else:
                fee += 0
                total_hr -= 1

            if (total_hr <= 2 and fee > 0):
                print(f"Total amount due is {fee} Baht, thank you.")
                break

        elif (fee != 0 or buyAmt >= 3001 or total_hr < 3):
            print("No charge, thank you.")
            break
