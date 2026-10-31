# University Scholarship Allocation System

students = []
eligible_students = []
not_eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))

    subjects = []
    for j in range(3):
        marks = float(input("Enter subject " + str(j + 1) + " marks: "))
        subjects.append(marks)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total_marks = sum(subjects)

    # Eligibility checking
    if (aggregate >= 75 and
        all(mark >= 60 for mark in subjects) and
        attendance >= 75 and
        income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "total": total_marks
        })

        eligible_students.append(name)

    else:
        not_eligible.append(name)

# Ranking eligible students
students.sort(
    key=lambda x: (
        x["aggregate"],
        x["attendance"],
        x["total"]
    ),
    reverse=True
)

# Display eligible students
print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if students:
    print("\nRank  Name       Aggregate  Attendance  Total Marks")

    for rank, student in enumerate(students, start=1):
        print(rank, student["name"],
              student["aggregate"],
              student["attendance"],
              student["total"])
else:
    print("No eligible students found.")

# Display not eligible students
print("\n===== NOT ELIGIBLE STUDENTS =====")

if not_eligible:
    for name in not_eligible:
        print(name)
else:
    print("All students are eligible.")









    

        






### 8\. Conclusion

The University Scholarship Allocation System successfully evaluates student applications using aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income. It identifies eligible students, ranks them based on merit, and resolves ties using predefined rules. This system reduces manual work and makes scholarship allocation systematic, transparent, and efficient.

Important note: This program uses illustrative eligibility criteria. Actual university scholarship rules may differ. The program ranks eligible students; it does not limit the number of scholarships awarded.

