
books = []

while True:
    print("\n--- LIBRARY MANAGEMENT ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        books.append({"name": name, "borrowed": False})
        print("Book added successfully!")

    elif choice == "2":
        if not books:
            print("Library is empty.")
        else:
            for book in books:
                status = "Borrowed" if book["borrowed"] else "Available"
                print(book["name"], "-", status)

    elif choice == "3":
        name = input("Enter book name to borrow: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True
                if not book["borrowed"]:
                    book["borrowed"] = True
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        name = input("Enter book name to return: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True
                if book["borrowed"]:
                    book["borrowed"] = False
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Library system closed.")
        break

    else:
        print("Invalid choice!")
