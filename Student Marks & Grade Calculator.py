def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

grade = calculate_grade(average)

print("\n===== RESULT =====")
print("Student Name :", name)
print("Marks        :", marks)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Highest Mark :", highest)
print("Lowest Mark  :", lowest)
print("Grade        :", grade)

if grade == "F":
    print("Result       : FAIL")
else:
    print("Result       : PASS")
