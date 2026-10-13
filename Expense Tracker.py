
expenses = []

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        if amount > 0:
            expenses.append({"name": name, "amount": amount})
            print("Expense added successfully!")
        else:
            print("Amount must be greater than zero.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for item in expenses:
                print(item["name"], "- ₹", item["amount"])

    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print("Total expenses: ₹", round(total, 2))

    elif choice == "4":
        if expenses:
            highest = max(expenses, key=lambda x: x["amount"])
            print("Highest expense:", highest["name"])
            print("Amount: ₹", highest["amount"])
        else:
            print("No expenses recorded.")

    elif choice == "5":
        print("Expense tracker closed.")
        break

    else:
        print("Invalid choice. Try again.")
