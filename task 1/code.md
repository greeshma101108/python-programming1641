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

```mermaid
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


## Sample Output

```text
===== SCHOLARSHIP ALLOCATION RESULTS =====

Rank  Name       Aggregate  Attendance  Total Marks
1     Priya      92.0       95.0        273.0
2     Ravi       85.0       90.0        255.0

===== NOT ELIGIBLE STUDENTS =====

Kumar
```


