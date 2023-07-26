target = 72

guess_num = int(input("Enter your guess (0 - 100): "))

if (guess_num < 0 or guess_num > 100):
    print("Sorry, out of range, try again later.")
else:
    if (guess_num == target):
        print("Congratulations, your guess is correct.")
    else:
        print("Sorry, your guess is wrong, try again later.")
