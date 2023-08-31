import time

input_num = int(input("Enter a number: "))


def factorial(number: int):
    i = number
    result = 1
    while i >= 1:
        result *= i
        i -= 1
    return display_cal_factorial(number, i, result)


count = 0


def display_cal_factorial(target_number: int, current_number: int, result: int):
    j = target_number
    nunm_str = "1" if (target_number <= 1) else ""
    while j >= 1 and target_number != 1:
        nunm_str += f"{j}" if (target_number == j) else f" x {j}"
        j -= 1

    display_str = f"{target_number}! = " + nunm_str + f" = {result}"
    return display_str


start = time.time()
if (input_num < 0):
    print("Invalid input, program terminates.")
else:
    while count <= input_num:
        print(factorial(count))
        count += 1
end = time.time()
