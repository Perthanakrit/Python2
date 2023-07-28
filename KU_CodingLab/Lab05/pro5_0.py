age = int(input("Enter your age: "))
nic = int(input("Enter your net income: "))

if age < 15 or age > 60:
    print("Invalid age.")
elif nic >= 80000:
    print("Invalid income.")
elif nic >= 1 and nic <= 30000:
    nit = nic*20/100
    print(f"Your negative income tax is {nit:.2f} Baht.")
elif nic > 30000 and nic <= 79999:
    nic = (80000 - nic) * 0.12
    # nit = nic*8/100
    print(f"Your negative income tax is {nic:.2f} Baht.")
