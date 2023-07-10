totalIncome = float(input())
expense = float(input())

# exp_str = str(expense).strip("-")
# expense = float(exp_str)

profit = (totalIncome + expense)

display_profit = "0" * (5 - len(str(int(profit)))) + f"{profit:.2f}"

print("Total Income{totalIncome:>9s} bahts".format(
    totalIncome=f"+{totalIncome:.2f}"))
print("Expense{expense:>14s} bahts".format(expense=f"{expense:.2f}"))
print("Profit{display_profit:>15} bahts".format(display_profit=display_profit))
