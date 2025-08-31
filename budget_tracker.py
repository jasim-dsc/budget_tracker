# Personal Budget Tracker

income = float(input("Enter your monthly income: "))
expenses = []

while True:
    expense = input("Enter expense (or type 'done' to finish): ")
    if expense.lower() == 'done':
        break
    amount = float(input(f"Enter amount for {expense}: "))
    expenses.append(amount)

total_expenses = sum(expenses)
balance = income - total_expenses

print(f"Total Expenses: {total_expenses}")
print(f"Remaining Balance: {balance}")
