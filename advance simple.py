while True:
    print("1. Add")
    print("2. subtract")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", a + b)
    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", a - b)
    elif choice == 3:
        print("Program end!")
        break
    else:
        print("Enter the correct number only....")
