'''
119 = 
'''


def is_not_prime(number: int):
    divisor = 2
    is_perfect = 2

    while divisor <= 9:

        if (number % divisor == 0 and divisor != number):
            is_perfect += 1

        divisor += 1

    return is_perfect > 2


def display(number: int):
    text = ""
    if (is_not_prime(number)):
        text = "not a prime"
    else:
        text = "a prime"

    return f"{number} is {text} number."


while True:
    input_number = int(input("Enter a number: "))
    if (input_number == 0):
        print("End of program, goodbye.")
        break
    elif (input_number != 0 and input_number <= 1):
        print("Invalid input, try again.")
    else:
        print(display(input_number))
