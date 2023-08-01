year_input = int(input("Enter year: "))

is_leap = (year_input % 4 == 0 and year_input %
           100 != 0) or year_input % 400 == 0

if (year_input >= 0 and type(year_input) == int):
    if (is_leap):
        print(f"{year_input} is a leap year.")
    else:
        print(f"{year_input} is not a leap year.")
else:
    print("Invalid year.")
