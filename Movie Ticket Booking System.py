
movies = {
    "1": {"name": "Leo", "price": 150, "seats": 50},
    "2": {"name": "Jailer", "price": 180, "seats": 40},
    "3": {"name": "Vikram", "price": 200, "seats": 30}
}

bookings = []

while True:
    print("\n===== MOVIE TICKET BOOKING =====")
    print("1. View Movies")
    print("2. Book Tickets")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for key, movie in movies.items():
            print(
                key, movie["name"],
                "- ₹", movie["price"],
                "- Available seats:", movie["seats"]
            )

    elif choice == "2":
        movie_id = input("Enter movie number: ")

        if movie_id not in movies:
            print("Invalid movie selection!")
            continue

        movie = movies[movie_id]
        quantity = int(input("Enter number of tickets: "))

        if quantity <= 0:
            print("Enter a valid ticket quantity.")

        elif quantity > movie["seats"]:
            print("Not enough seats available.")

        else:
            total = quantity * movie["price"]

            print("Movie:", movie["name"])
            print("Tickets:", quantity)
            print("Total price: ₹", total)

            confirm = input("Confirm booking? (yes/no): ").lower()

            if confirm == "yes":
                movie["seats"] -= quantity

                bookings.append({
                    "movie": movie["name"],
                    "tickets": quantity,
                    "total": total
                })

                print("Booking successful!")
            else:
                print("Booking cancelled.")

    elif choice == "3":
        if not bookings:
            print("No bookings found.")
        else:
            for booking in bookings:
                print("\nMovie:", booking["movie"])
                print("Tickets:", booking["tickets"])
                print("Total: ₹", booking["total"])

    elif choice == "4":
        print("Thank you for using our booking system!")
        break

    else:
        print("Invalid choice!")
