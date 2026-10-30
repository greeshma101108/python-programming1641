
# University Scholarship Allocation System
students = []
eligible_students = []

# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000
n = int(input("Enter number of students: "))

# Collect Student Details
for i in range(n):
    print("\nEnter details of Student", i + 1)
    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks (%): "))
    print("Enter marks of 3 subjects:")
    subject1 = float(input("Subject 1: "))
    subject2 = float(input("Subject 2: "))
    subject3 = float(input("Subject 3: "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income: "))
    # Check Eligibility
    if (aggregate >= MIN_AGGREGATE and
        subject1 >= MIN_SUBJECT_MARK and
        subject2 >= MIN_SUBJECT_MARK and
        subject3 >= MIN_SUBJECT_MARK and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):
        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "subject_total": subject1 + subject2 + subject3
        })
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")

# Sort Eligible Students
students.sort(
    key=lambda x: (
        x["aggregate"],
        x["attendance"],
        x["subject_total"]
    ),
    reverse=True
)

# Display Final Ranking
print("\n===== SCHOLARSHIP ALLOCATION LIST =====")

if len(students) == 0:
    print("No eligible students found.")

else:
    print("Rank\tName\t\tAggregate\tAttendance")
    for rank, student in enumerate(students, start=1):
        print(
            rank, "\t",
            student["name"], "\t",
            student["aggregate"], "\t\t",
            student["attendance"]
        )

print("\nTotal Eligible Students:", len(students))
print("Total Rejected Students:", n - len(students))

