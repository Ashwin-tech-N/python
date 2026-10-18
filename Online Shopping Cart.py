
products = {
    "laptop": 50000,
    "phone": 20000,
    "headphones": 1500,
    "mouse": 800
}

cart = {}

while True:
    print("\n===== ONLINE SHOPPING =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for name, price in products.items():
            print(name, "- ₹", price)

    elif choice == "2":
        name = input("Enter product name: ").lower()

        if name in products:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[name] = cart.get(name, 0) + quantity
                print("Product added!")
            else:
                print("Quantity must be positive.")
        else:
            print("Product not available.")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            total = 0

            for name, quantity in cart.items():
                cost = products[name] * quantity
                print(name, "x", quantity, "= ₹", cost)
                total += cost

            print("Cart Total: ₹", total)

    elif choice == "4":
        name = input("Enter product to remove: ").lower()

        if name in cart:
            del cart[name]
            print("Product removed.")
        else:
            print("Product not found in cart.")

    elif choice == "5":
        total = sum(
            products[name] * quantity
            for name, quantity in cart.items()
        )

        if total == 0:
            print("Your cart is empty.")
        else:
            print("Final Bill: ₹", total)
            print("Order placed successfully!")
            cart.clear()

    elif choice == "6":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")
