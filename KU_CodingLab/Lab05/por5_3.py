odd_count = 0

while (True):
    input_num = int(input("Enter number: "))
    if (input_num < 0):
        print(f"Received {odd_count} odd numbers")
        break
    else:
        if (input_num % 2 != 0):
            odd_count += 1
