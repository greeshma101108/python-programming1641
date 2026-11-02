### Comprehensive Smart Campus Management Simulation – Python Program

### 1\. Problem Statement

The Comprehensive Smart Campus Management Simulation is a menu-driven Python application designed to manage different campus activities in one program.

The system integrates student records, attendance management, marks calculation, event registration, resource allocation and summary reporting.

The program performs the following operations:

* Student Records: Stores student ID, name, department and year.

* Attendance Management: Records the number of classes attended and conducted and calculates attendance percentage.

* Marks Management: Accepts marks in multiple subjects and calculates total and average marks.

* Event Registration: Allows students to register for campus events.

* Resource Allocation: Allocates available campus resources such as projectors, laboratories and seminar halls.

* Summary Reporting: Displays student details, attendance, marks, event registrations and allocated resources.

The program uses conditional statements, loops, strings, lists, nested lists, tuples and tuple unpacking.

### 2\. Algorithm

* Start the program.

* Initialize empty lists for student records, attendance, marks, events and resources.

* Display the main menu.

* Ask the user to select an operation.

* Perform the selected operation:

    * Option 1 – Add Student: Enter student ID, name, department and year. Store the details.

    * Option 2 – Attendance: Enter student ID, classes attended and total classes. Calculate attendance percentage.

    * Option 3 – Marks: Enter student ID and marks in three subjects. Calculate total and average.

    * Option 4 – Event Registration: Enter student ID and event name. Store the registration.

    * Option 5 – Resource Allocation: Enter resource name and allocate it if available.

    * Option 6 – Summary Report: Display all stored student information and campus activities.

    * Option 7 – Exit: Terminate the program.

* If the selected option is invalid, display an error message.

* Repeat the menu until the user selects Exit.

* Stop the program.

### 3\. Flowchart

```mermaid
flowchart TD
    A([START]) --> B[Initialize Empty Lists]
    B --> C[Display Main Menu]
    C --> D[/Enter Menu Choice/]

    D --> E{Select Operation}

    E -- 1 --> F[/Enter Student Details/]
    F --> G[Store Student Record]
    G --> C

    E -- 2 --> H[/Enter Student ID and Attendance Details/]
    H --> I[Calculate Attendance Percentage]
    I --> J[Store Attendance Record]
    J --> C

    E -- 3 --> K[/Enter Student ID and Subject Marks/]
    K --> L[Calculate Total and Average Marks]
    L --> M[Store Marks Record]
    M --> C

    E -- 4 --> N[/Enter Student ID and Event Name/]
    N --> O[Store Event Registration]
    O --> C

    E -- 5 --> P[/Enter Resource Name/]
    P --> Q{Is Resource Available?}
    Q -- Yes --> R[Allocate Resource]
    Q -- No --> S[Display Resource Not Available]
    R --> C
    S --> C

    E -- 6 --> T[Generate Campus Summary Report]
    T --> U[Display Student Attendance Marks Events and Resources]
    U --> C

    E -- 7 --> V([STOP])

    E -- Invalid --> W[/Display Invalid Choice/]
    W --> C
```
### 5\. Sample Input

The following is a simple example of entering student details, attendance, marks, event registration and resource allocation.

```text
===== SMART CAMPUS MANAGEMENT =====
1. Add Student Record
2. Attendance Management
3. Marks Management
4. Event Registration
5. Resource Allocation
6. Summary Report
7. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Ravi
Enter Department: CSE
Enter Year: 1

Student record added successfully!

Enter your choice: 2

Enter Student ID: 101
Enter classes attended: 45
Enter total classes conducted: 50

Attendance Percentage: 90.0 %

Enter your choice: 3

Enter Student ID: 101
Enter Subject 1 marks: 85
Enter Subject 2 marks: 90
Enter Subject 3 marks: 80

Total Marks: 255.0
Average Marks: 85.0

Enter your choice: 4

Enter Student ID: 101
Enter Event Name: Coding Competition

Event registration successful!

Enter your choice: 5

Enter Resource Name: Projector

Projector allocated successfully!

Enter your choice: 6
```

### 6\. Sample Output

```text
===== CAMPUS SUMMARY REPORT =====

--- STUDENT RECORDS ---
101 Ravi CSE 1

--- ATTENDANCE DETAILS ---
101 45 / 50 Attendance: 90.0 %

--- MARKS DETAILS ---
101 Total: 255.0 Average: 85.0

--- EVENT REGISTRATIONS ---
101 registered for Coding Competition

--- RESOURCE AVAILABILITY ---
Projector Available: 1
Laboratory Available: 1
Seminar Hall Available: 1

Enter your choice: 7

Exiting Smart Campus Management System.
```


* `all()` function

Note: This is a basic educational simulation. The records are stored in memory and will be cleared when the program exits. It does not use a database.
