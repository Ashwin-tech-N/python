
def calculate_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + (units - 100) * 2.5
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5)
        bill += (units - 200) * 4
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4)
        bill += (units - 300) * 6

    service_charge = 50
    return bill + service_charge


while True:
    print("\n===== ELECTRICITY BILL =====")
    print("1. Calculate Bill")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            units = float(input("Enter units consumed: "))

            if units < 0:
                print("Units cannot be negative.")
            else:
                total = calculate_bill(units)
                print("Units consumed:", units)
                print("Total electricity bill: ₹", round(total, 2))

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
