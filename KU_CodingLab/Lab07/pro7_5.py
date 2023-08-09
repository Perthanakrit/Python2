err_mess_num, err_mess_digit = "", ""
input_num = int(input("Enter a number: "))
if (input_num < 0):
    err_mess_num = "Invalid number."
digit = int(input("Enter a digit: "))
if (digit >= 9 or digit < 0):
    err_mess_digit = "Invalid digit."

if (input_num >= 0 and 0 <= digit <= 9):
    num = 0
    count = 0

    while True:
        num = input_num % 10
        input_num //= 10

        if (digit == num):
            count += 1
            if (input_num <= 0):
                break
        if (input_num <= 0):
            break

    s_char = "" if (0 < count <= 1) else "s"
    print(f"Digit {digit} occurs {count} time{s_char}.")

elif (input_num < 0 or digit >= 9 or digit < 0):
    if (err_mess_num != ""):
        print(err_mess_num)
    if (err_mess_digit != ""):
        print(err_mess_digit)
