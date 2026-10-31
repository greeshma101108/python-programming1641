### University Scholarship Allocation System – Python Program

### 1\. Problem Statement

The University Scholarship Allocation System is designed to evaluate students who apply for scholarships based on their academic performance and eligibility criteria.

The system considers the following factors:

* Aggregate Marks: Students must score at least 75% in aggregate.

* Subject-wise Minimum Marks: Students must score at least 60 marks in every subject.

* Attendance: Students must have at least 75% attendance.

* Family Income: Annual family income must not exceed ₹2,50,000.

* Ranking: Eligible students are ranked according to their aggregate marks.

* Tie-Breaking Rules: If two students have equal aggregate marks, the student with higher attendance gets the higher rank. If attendance is also equal, the student with higher total subject marks gets priority.

The program identifies eligible students, ranks them, and displays the final scholarship allocation list.

### 2\. Algorithm

Step 1: Start the program.

Step 2: Enter the number of students.

Step 3: For each student, enter:

* Student name

* Aggregate percentage

* Subject marks

* Attendance percentage

* Annual family income

Step 4: Check eligibility conditions:

* Aggregate marks ≥ 75%.

* Each subject mark ≥ 60.

* Attendance ≥ 75%.

* Family income ≤ ₹2,50,000.

Step 5: If all conditions are satisfied, add the student to the eligible list.

Step 6: Sort eligible students using the following priority:

* Higher aggregate percentage.

* Higher attendance percentage.

* Higher total subject marks.

Step 7: Assign ranks to eligible students.

Step 8: Display eligible students with their ranks.

Step 9: Display students who are not eligible.

Step 10: Stop the program.
...mermid
### 3\. Flowchart

START

Enter number of students

Enter student details and marks

Check eligibility criteria

Marks, subjects, attendance and income

YES

Add to eligible list

NO

Mark as not eligible

Sort eligible students by marks, attendance and subject total

Assign ranks to students

Display scholarship results

STOP

### 4\. Python Source Code

```python
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
```

### 5\. Sample Input

```text
Enter number of students: 3

Enter details of Student 1
Enter student name: Ravi
Enter aggregate percentage: 85
Enter subject 1 marks: 80
Enter subject 2 marks: 85
Enter subject 3 marks: 90
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Priya
Enter aggregate percentage: 92
Enter subject 1 marks: 95
Enter subject 2 marks: 90
Enter subject 3 marks: 88
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Kumar
Enter aggregate percentage: 70
Enter subject 1 marks: 65
Enter subject 2 marks: 70
Enter subject 3 marks: 75
Enter attendance percentage: 80
Enter annual family income: 200000
```

### 6\. Sample Output

```text
===== SCHOLARSHIP ALLOCATION RESULTS =====

Rank  Name       Aggregate  Attendance  Total Marks

1     Priya      92.0       95.0        273.0
2     Ravi       85.0       90.0        255.0

===== NOT ELIGIBLE STUDENTS =====

Kumar
```

### 7\. Explanation of Output

* Priya: Eligible because she satisfies all four eligibility conditions. She gets Rank 1 because she has the highest aggregate percentage.

* Ravi: Eligible because he satisfies all four eligibility conditions. He gets Rank 2.

* Kumar: Not eligible because his aggregate percentage is only 70%, which is below the required 75%.

### 8\. Conclusion

The University Scholarship Allocation System successfully evaluates students based on academic marks, subject-wise performance, attendance, and family income. It identifies eligible students, ranks them according to predefined tie-breaking rules, and displays the final scholarship allocation results.

This program demonstrates important Python concepts such as:

* Conditional statements (`if-else`)

* Loops (`for`)

* Lists and dictionaries

* Functions (`sum`, `all`)

* Sorting using `sort()`

* Lambda expressions

These concepts are useful for a B.Tech 1st-year Python programming practical examination.



        







