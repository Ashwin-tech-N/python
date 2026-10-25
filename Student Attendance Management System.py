
students = {}

while True:
    print("\n===== ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            students[name] = {"present": 0, "total": 0}
            print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name not in students:
            print("Student not found.")
        else:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P" or status == "A":
                students[name]["total"] += 1

                if status == "P":
                    students[name]["present"] += 1
                    print("Marked Present.")
                else:
                    print("Marked Absent.")
            else:
                print("Invalid attendance status.")

    elif choice == "3":
        if not students:
            print("No students registered.")
        else:
            for name, data in students.items():
                total = data["total"]
                present = data["present"]

                percentage = (
                    present / total * 100 if total > 0 else 0
                )

                print("\nStudent:", name)
                print("Classes:", total)
                print("Present:", present)
                print("Attendance:", round(percentage, 2), "%")

                if total > 0 and percentage < 75:
                    print("Warning: Attendance below 75%")

    elif choice == "4":
        print("Attendance system closed.")
        break

    else:
        print("Invalid choice!")
