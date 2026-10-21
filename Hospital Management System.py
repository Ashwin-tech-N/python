
patients = []

def register_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter health issue: ")

    patients.append({
        "name": name,
        "age": age,
        "disease": disease,
        "bill": 0
    })

    print("Patient registered successfully!")

while True:
    print("\n===== HOSPITAL MANAGEMENT =====")
    print("1. Register Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        if not patients:
            print("No patient records found.")
        else:
            for patient in patients:
                print("\nName:", patient["name"])
                print("Age:", patient["age"])
                print("Health issue:", patient["disease"])
                print("Bill: ₹", patient["bill"])

    elif choice == "3":
        name = input("Enter patient name: ").lower()
        found = False

        for patient in patients:
            if patient["name"].lower() == name:
                print("Patient found:", patient["name"])
                print("Health issue:", patient["disease"])
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == "4":
        name = input("Enter patient name: ").lower()
        found = False

        for patient in patients:
            if patient["name"].lower() == name:
                consultation = float(
                    input("Enter consultation fee: ")
                )
                medicine = float(input("Enter medicine cost: "))

                if consultation < 0 or medicine < 0:
                    print("Costs cannot be negative.")
                else:
                    patient["bill"] = consultation + medicine
                    print("Total bill: ₹", patient["bill"])

                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == "5":
        print("Hospital system closed.")
        break

    else:
        print("Invalid choice!")
