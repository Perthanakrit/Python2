target_digit = int(input("Enter a target (4-digit integer): "))
guess_digit = int(input("Enter your guess (4-digit integer): "))

n1 = guess_digit % 10
n2 = guess_digit//10 % 10
n3 = guess_digit//100 % 10
n4 = guess_digit//1000 % 10

match_digit = 0
match_position = 0
CONST_GUESS_DIGIT = guess_digit

if target_digit == guess_digit:
    print("Congratulations, you just mastered my mind!!")
else:
    
    while True:

        digit_in_target = target_digit % 10
        target_digit //= 10
        digit_in_guess = guess_digit % 10
        guess_digit //= 10

        if (digit_in_target == n1 or digit_in_target == n2  or digit_in_target == n3 or digit_in_target == n4) and digit_in_target != digit_in_guess:
            
            match_digit += 1
     
        if (digit_in_target == digit_in_guess):
            match_position += 1

        if (target_digit <= 0 or guess_digit <= 0):
            break

    text_pos = ""
    text_digit = ""

    if (match_position == 0):
        text_pos = "No positions"
    elif (match_position == 1):
        text_pos = "One position"
    elif (match_position == 2):
        text_pos = "Two positions"
    elif (match_position == 3):
        text_pos = "Three positions"
    elif (match_position == 4):
        text_pos = "Four positions"

    if (match_digit == 0):
        text_digit = "no digits"
    elif (match_digit == 1):
        text_digit = "one digit"
    elif (match_digit == 2):
        text_digit = "two digits"
    elif (match_digit == 3):
        text_digit = "three digits"
    elif (match_digit == 4):
        text_digit = "four digits"

    print(f"{text_pos} correct, {text_digit} correct")