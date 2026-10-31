# University Scholarship Allocation System

## Aim

To design and implement a Python program that evaluates students for a university scholarship based on academic performance, subject-wise marks, attendance, and family income, and then ranks the eligible candidates.

## Problem Statement

The University Scholarship Allocation System is designed to identify students who are eligible for scholarship allocation based on predefined criteria. The program accepts details of multiple students, checks their eligibility, sorts the eligible students according to merit, and displays the final scholarship results.

The system considers the following rules:

- Aggregate Marks: A student must have at least 75% aggregate marks.
- Subject-wise Minimum Marks: A student must secure at least 60 marks in each subject.
- Attendance: A student must have at least 75% attendance.
- Family Income: The annual family income must be less than or equal to ₹2,50,000.
- Ranking: Eligible students are ranked according to their aggregate percentage.
- Tie-Breaking Rules: If two students have the same aggregate percentage, the student with higher attendance is ranked first. If attendance is also the same, the student with higher total subject marks gets priority.

The program identifies eligible candidates, arranges them in order of merit, and displays the final scholarship allocation list.

## Algorithm

1. Start the program.
2. Read the number of students.
3. For each student, input the following details:
   - Student name
   - Aggregate percentage
   - Marks of three subjects
   - Attendance percentage
   - Annual family income
4. Check the eligibility conditions:
   - Aggregate marks must be greater than or equal to 75
   - Each subject mark must be greater than or equal to 60
   - Attendance must be greater than or equal to 75
   - Family income must be less than or equal to 250000
5. If all conditions are satisfied, add the student to the eligible list.
6. Otherwise, add the student to the not eligible list.
7. Sort the eligible students according to:
   - Higher aggregate percentage
   - Higher attendance percentage
   - Higher total subject marks
8. Assign ranks to the eligible students.
9. Display the final list of eligible students along with their ranks.
10. Display the list of students who are not eligible.
11. Stop the program.

## Flowchart

```text
START
   |
   v
Enter number of students
   |
   v
Enter student details and marks
   |
   v
Check eligibility criteria
   |
   v
If eligible:
   - Add student to eligible list
Else:
   - Add student to not eligible list
   |
   v
Sort students by aggregate, attendance, and total marks
   |
   v
Assign ranks
   |
   v
Display scholarship results
   |
   v
STOP
```

## Python Source Code

```python
# University Scholarship Allocation System

students = []
not_eligible = []

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))

    subjects = []
    for j in range(3):
        marks = float(input(f"Enter subject {j + 1} marks: "))
        subjects.append(marks)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total_marks = sum(subjects)

    if (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARK for mark in subjects)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
    ):
        students.append(
            {
                "name": name,
                "aggregate": aggregate,
                "attendance": attendance,
                "total": total_marks,
            }
        )
    else:
        not_eligible.append(name)

students.sort(
    key=lambda x: (x["aggregate"], x["attendance"], x["total"]),
    reverse=True,
)

print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if students:
    print("\nRank  Name       Aggregate  Attendance  Total Marks")
    for rank, student in enumerate(students, start=1):
        print(
            f"{rank:<4} {student['name']:<10} {student['aggregate']:<9} "
            f"{student['attendance']:<10} {student['total']}"
        )
else:
    print("No eligible students found.")

print("\n===== NOT ELIGIBLE STUDENTS =====")

if not_eligible:
    for name in not_eligible:
        print(name)
else:
    print("All students are eligible.")
```

## Sample Input

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

## Sample Output

```text
===== SCHOLARSHIP ALLOCATION RESULTS =====

Rank  Name       Aggregate  Attendance  Total Marks
1     Priya      92.0       95.0        273.0
2     Ravi       85.0       90.0        255.0

===== NOT ELIGIBLE STUDENTS =====

Kumar
```

## Explanation of Output

- Priya is eligible because she satisfies all the required conditions. She ranks first because she has the highest aggregate percentage.
- Ravi is eligible because he also satisfies all the conditions. He ranks second.
- Kumar is not eligible because his aggregate percentage is only 70%, which is below the required 75%.

## Conclusion

The University Scholarship Allocation System demonstrates how Python can be used to process student data, apply eligibility conditions, sort candidates based on merit, and display final results. This system is useful for understanding decision-making, list handling, loops, sorting, and dictionary-based data storage in Python programming.

The program helps in evaluating scholarship candidates efficiently and provides a clear ranking of eligible students. It also helps in understanding the practical application of conditional statements and sorting techniques in a real-world academic scenario.

This project is suitable for a B.Tech first-year Python practical assignment and demonstrates key programming concepts such as:

- Conditional statements (`if-else`)
- Loops (`for`)
- Lists and dictionaries
- Built-in functions such as `sum()` and `all()`
- Sorting using `sort()`
- Lambda expressions
