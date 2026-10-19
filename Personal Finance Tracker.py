
transactions = []

def add_transaction(transaction_type, amount, category):
    transactions.append({
        "type": transaction_type,
        "amount": amount,
        "category": category
    })
    print("Transaction added successfully!")

while True:
    print("\n===== FINANCE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Financial Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        if amount <= 0:
            print("Amount must be positive.")
            continue

        if choice == "1":
            add_transaction("Income", amount, category)
        else:
            add_transaction("Expense", amount, category)

    elif choice == "3":
        if not transactions:
            print("No transactions found.")
        else:
            for t in transactions:
                print(
                    t["type"], "-",
                    t["category"], "- ₹",
                    t["amount"]
                )

    elif choice == "4":
        income = sum(
            t["amount"] for t in transactions
            if t["type"] == "Income"
        )

        expenses = sum(
            t["amount"] for t in transactions
            if t["type"] == "Expense"
        )

        print("\nTotal Income: ₹", income)
        print("Total Expenses: ₹", expenses)
        print("Remaining Balance: ₹", income - expenses)

    elif choice == "5":
        print("Finance tracker closed.")
        break

    else:
        print("Invalid choice!")
