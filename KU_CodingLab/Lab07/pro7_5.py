err_mess = ""
input_num = int(input("Enter a number: "))
if (input_num < 0):
    err_mess = "Invalid number."
digit = int(input("Enter a digit: "))
if (digit >= 9 or digit < 0):
    err_mess = "Invalid digit."

if (input_num >= 0 and 0 <= digit <= 9):
    num = 0
    count = 0

    while input_num > 0:
        num = input_num % 10
        input_num //= 10

        if (digit == num):
            count += 1

    s_char = "" if (0 < count <= 1) else "s"
    print(f"Digit {digit} occurs {count} time{s_char}.")

elif (err_mess != ""):
    print(err_mess)
