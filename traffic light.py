
while True:
    print("\n===== TRAFFIC LIGHT SYSTEM =====")
    print("1. Red")
    print("2. Yellow")
    print("3. Green")
    print("4. Exit")

    choice = input("Enter traffic light color: ")

    if choice == "1":
        print("🔴 RED - STOP!")
    elif choice == "2":
        print("🟡 YELLOW - GET READY!")
    elif choice == "3":
        print("🟢 GREEN - GO!")
    elif choice == "4":
        print("Traffic system closed.")
        break
    else:
        print("Invalid choice!")

