target = 72

input_num = int(input("Enter your guess (0 - 100): "))

if (input_num == target):
    print("Congratulations, your guess is correct.")
elif (input_num < target):
    if (input_num >= 0):
        print("Sorry, your guess is too low, try again later.")
    else:
        print("Sorry, out of range, try again later.")
elif (input_num > target):
    if (input_num <= 100):
        print("Sorry, your guess is too high, try again later.")
    else:
        print("Sorry, out of range, try again later.")
