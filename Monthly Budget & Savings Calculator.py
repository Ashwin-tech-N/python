
income = float(input("Enter your monthly income: ₹"))

expenses = {}

categories = ["Food", "Travel", "Shopping", "Education", "Other"]

for category in categories:
    amount = float(input(f"Enter {category} expenses: ₹"))
    expenses[category] = amount

total_expenses = sum(expenses.values())
balance = income - total_expenses

print("\n===== MONTHLY REPORT =====")

for category, amount in expenses.items():
    print(category, ": ₹", amount)

print("\nMonthly Income: ₹", income)
print("Total Expenses: ₹", total_expenses)
print("Remaining Balance: ₹", balance)

if income > 0:
    savings_percentage = (balance / income) * 100
    print("Savings Percentage:", round(savings_percentage, 2), "%")

if balance < 0:
    print("Warning: You are spending more than your income!")
elif balance == 0:
    print("You have used your entire income.")
else:
    print("Good! You have money remaining.")
