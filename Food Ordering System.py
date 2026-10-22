
menu = {
    "pizza": 250,
    "burger": 120,
    "pasta": 180,
    "sandwich": 100,
    "juice": 60
}

cart = {}

while True:
    print("\n===== FOOD ORDERING SYSTEM =====")
    print("1. View Menu")
    print("2. Order Food")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for food, price in menu.items():
            print(f"{food.title()} - ₹{price}")

    elif choice == "2":
        food = input("Enter food name: ").lower()

        if food in menu:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[food] = cart.get(food, 0) + quantity
                print("Item added to cart!")
            else:
                print("Quantity must be positive.")
        else:
            print("Food item not available.")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            total = 0

            for food, quantity in cart.items():
                cost = menu[food] * quantity
                print(f"{food.title()} x {quantity} = ₹{cost}")
                total += cost

            print("Subtotal: ₹", total)

    elif choice == "4":
        total = sum(
            menu[food] * quantity
            for food, quantity in cart.items()
        )

        if total == 0:
            print("Your cart is empty.")
            continue

        discount = total * 0.10 if total >= 500 else 0
        final_bill = total - discount

        print("\nSubtotal: ₹", total)
        print("Discount: ₹", discount)
        print("Final Bill: ₹", final_bill)
        print("Order placed successfully!")

        cart.clear()

    elif choice == "5":
        print("Thank you for ordering!")
        break

    else:
        print("Invalid choice. Try again.")
