
contacts = {}

while True:
    print("\n===== CONTACT MANAGER =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        if phone.isdigit() and len(phone) == 10:
            contacts[name.lower()] = {
                "name": name,
                "phone": phone
            }
            print("Contact added successfully!")
        else:
            print("Enter a valid 10-digit phone number.")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for contact in contacts.values():
                print(contact["name"], ":", contact["phone"])

    elif choice == "3":
        name = input("Enter name to search: ").lower()

        if name in contacts:
            print("Name:", contacts[name]["name"])
            print("Phone:", contacts[name]["phone"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ").lower()

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Contact manager closed.")
        break

    else:
        print("Invalid choice!")
