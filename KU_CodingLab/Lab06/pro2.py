target = 72
count = 0
while True:
    your_guess = int(input("Enter your guess: "))

    count += 1

    if your_guess < 0 or your_guess > 100:
        print("Sorry, your guess is out of range.")
    else:
        if your_guess < target:
            print("Sorry, your guess is too low.")
        elif your_guess > target:
            print("Sorry, your guess is too high.")
        elif your_guess == target:
            break


print("Congratulations, your guess is correct.")
print(f"Total number of guesses is {count}.")
