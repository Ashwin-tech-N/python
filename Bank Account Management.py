
balance = 1000
history = []

while True:
    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            history.append(f"Deposited: ₹{amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount <= balance:
            balance -= amount
            history.append(f"Withdrawn: ₹{amount}")
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        if len(history) == 0:
            print("No transactions yet.")
        else:
            for transaction in history:
                print(transaction)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
