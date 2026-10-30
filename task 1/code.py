### UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM

B.Tech 1st Year – Python Programming

### 1\. Problem Statement

Design and develop a Python program for a University Scholarship Allocation System. The system evaluates students based on their aggregate marks, subject-wise minimum marks, attendance percentage, and family annual income.

The program should:

* Accept student details such as name, aggregate marks, subject marks, attendance, and annual family income.

* Check whether the student satisfies all scholarship eligibility criteria.

* Select only eligible students for the scholarship.

* Rank eligible students based on their aggregate marks.

* Resolve ties using predefined rules:

    * Higher aggregate marks.

    * Higher attendance percentage.

    * Higher subject-wise marks.

* Display the final scholarship allocation list with student ranks.

### 2\. Algorithm

Step 1: Start the program.

Step 2: Read the number of students.

Step 3: Set the scholarship eligibility criteria:

* Aggregate marks ≥ 75%.

* Each subject mark ≥ 50%.

* Attendance ≥ 75%.

* Annual family income ≤ ₹2,50,000.

Step 4: Enter each student's details:

* Student name.

* Aggregate marks.

* Subject-wise marks.

* Attendance percentage.

* Annual family income.

Step 5: Check all eligibility conditions.

Step 6: If all conditions are satisfied, add the student to the eligible list. Otherwise, reject the application.

Step 7: Sort eligible students according to:

* Aggregate marks (descending).

* Attendance (descending).

* Subject-wise marks (descending).

Step 8: Assign ranks to eligible students.

Step 9: Display the final scholarship allocation list.

Step 10: Stop the program.

### 3\. Flowchart

START

Enter number of students

Enter student details and marks

Check eligibility criteria

Marks, subjects, attendance and income

YES

Add to eligible list

NO

Reject application

Sort eligible students by marks, attendance and subject marks

Assign student ranks

Display scholarship list

STOP

### 4\. Python Source Code

```python

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
```

### 5\. Sample Input

```text
Enter number of students: 4

Enter details of Student 1
Enter student name: Rahul
Enter aggregate marks (%): 85
Enter marks of 3 subjects:
Subject 1: 80
Subject 2: 75
Subject 3: 90
Enter attendance (%): 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Priya
Enter aggregate marks (%): 92
Enter marks of 3 subjects:
Subject 1: 95
Subject 2: 90
Subject 3: 88
Enter attendance (%): 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Arun
Enter aggregate marks (%): 78
Enter marks of 3 subjects:
Subject 1: 70
Subject 2: 65
Subject 3: 75
Enter attendance (%): 80
Enter annual family income: 220000

Enter details of Student 4
Enter student name: Sneha
Enter aggregate marks (%): 65
Enter marks of 3 subjects:
Subject 1: 60
Subject 2: 55
Subject 3: 70
Enter attendance (%): 85
Enter annual family income: 150000
```

### 6\. Sample Output

```text
Eligible for Scholarship
Eligible for Scholarship
Eligible for Scholarship
Not Eligible for Scholarship

===== SCHOLARSHIP ALLOCATION LIST =====

Rank    Name       Aggregate    Attendance
1       Priya      92.0         95.0
2       Rahul      85.0         90.0
3       Arun       78.0         80.0

Total Eligible Students: 3
Total Rejected Students: 1
```

### 7\. Explanation of Python Concepts Used

| Python concept | Purpose                           |
| -------------- | --------------------------------- |
| input()        | Accepts student details           |
| for loop       | Repeats data entry                |
| if-else        | Checks eligibility                |
| list           | Stores eligible students          |
| dictionary     | Stores individual student details |
| sort()         | Arranges students by merit        |
| lambda         | Defines sorting conditions        |
| enumerate()    | Assigns student ranks             |

### 8\. Conclusion

The University Scholarship Allocation System successfully evaluates student applications using aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income. It identifies eligible students, ranks them based on merit, and resolves ties using predefined rules. This system reduces manual work and makes scholarship allocation systematic, transparent, and efficient.

Important note: This program uses illustrative eligibility criteria. Actual university scholarship rules may differ. The program ranks eligible students; it does not limit the number of scholarships awarded.

