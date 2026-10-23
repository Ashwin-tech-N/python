
pin = "1234"
attempts = 3
unlocked = False

while attempts > 0:
    entered_pin = input("Enter your mobile PIN: ")

    if entered_pin == pin:
        print("\nMobile unlocked successfully!")
        unlocked = True
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts remaining:", attempts)

if not unlocked:
    print("Mobile locked. Try again later.")

else:
    while True:
        print("\n===== MOBILE MENU =====")
        print("1. Change PIN")
        print("2. Lock Mobile")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            old_pin = input("Enter your current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if new_pin.isdigit() and len(new_pin) == 4:
                    confirm_pin = input("Confirm new PIN: ")

                    if new_pin == confirm_pin:
                        pin = new_pin
                        print("PIN changed successfully!")
                    else:
                        print("PINs do not match.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == "2":
            print("Mobile locked successfully!")
            break

        elif choice == "3":
            print("Exiting mobile system.")
            break

        else:
            print("Invalid choice!")
