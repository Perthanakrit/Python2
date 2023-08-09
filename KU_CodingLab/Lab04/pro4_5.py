your_age = int(input("Enter your age: "))
your_next_income = int(input("Enter your net income: "))
nit_money = 0

if (15 <= your_age <= 60):
    if (1 <= your_next_income < 80000):
        if (your_next_income <= 30000):
            nit_money = your_next_income * (20/100)
        elif (your_next_income > 30000):
            nit_money = (12/100) * (80000 - your_next_income)
        print("Your negative income tax is {0:.2f} Baht. ".format(nit_money))

    else:
        print("Invalid income.")
else:
    print("Invalid age.")
