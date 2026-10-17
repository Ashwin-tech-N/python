
employees = []

while True:
    print("\n--- EMPLOYEE SALARY SYSTEM ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = float(input("Enter basic salary: "))
        allowance = float(input("Enter allowance: "))
        deduction = float(input("Enter deduction: "))

        if basic < 0 or allowance < 0 or deduction < 0:
            print("Salary values cannot be negative.")
            continue

        net_salary = basic + allowance - deduction

        employees.append({
            "name": name,
            "id": emp_id,
            "salary": net_salary
        })

        print("Employee added successfully!")

    elif choice == "2":
        if not employees:
            print("No employee records found.")
        else:
            for emp in employees:
                print("\nName:", emp["name"])
                print("ID:", emp["id"])
                print("Net Salary: ₹", round(emp["salary"], 2))

    elif choice == "3":
        emp_id = input("Enter employee ID: ")
        found = False

        for emp in employees:
            if emp["id"] == emp_id:
                print("Name:", emp["name"])
                print("Net Salary: ₹", round(emp["salary"], 2))
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")
