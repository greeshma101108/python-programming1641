
# Comprehensive Smart Campus Management Simulation

# Initialize lists
students = []
attendance = []
marks = []
registrations = []
resources = [
    ("Projector", 2),
    ("Laboratory", 1),
    ("Seminar Hall", 1)
]

while True:

    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student Record")
    print("2. Attendance Management")
    print("3. Marks Management")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Student Records
    if choice == "1":

        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        year = input("Enter Year: ")

        students.append((sid, name, department, year))

        print("Student record added successfully!")

    # 2. Attendance Management
    elif choice == "2":

        sid = input("Enter Student ID: ")
        attended = int(input("Enter classes attended: "))
        total = int(input("Enter total classes conducted: "))

        if total > 0 and 0 <= attended <= total:

            percentage = (attended / total) * 100

            attendance.append(
                (sid, attended, total, percentage)
            )

            print("Attendance Percentage:",
                  round(percentage, 2), "%")

        else:
            print("Invalid attendance details!")

    # 3. Marks Management
    elif choice == "3":

        sid = input("Enter Student ID: ")

        m1 = float(input("Enter Subject 1 marks: "))
        m2 = float(input("Enter Subject 2 marks: "))
        m3 = float(input("Enter Subject 3 marks: "))

        if all(0 <= m <= 100 for m in [m1, m2, m3]):

            total_marks = m1 + m2 + m3
            average = total_marks / 3

            marks.append(
                [sid, m1, m2, m3, total_marks, average]
            )

            print("Total Marks:", total_marks)
            print("Average Marks:", round(average, 2))

        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    # 4. Event Registration
    elif choice == "4":

        sid = input("Enter Student ID: ")
        event = input("Enter Event Name: ")

        registrations.append((sid, event))

        print("Event registration successful!")

    # 5. Resource Allocation
    elif choice == "5":

        resource_name = input("Enter Resource Name: ")

        found = False

        for i in range(len(resources)):

            resource, available = resources[i]

            if resource.lower() == resource_name.lower():

                found = True

                if available > 0:

                    resources[i] = (resource, available - 1)

                    print(resource, "allocated successfully!")

                else:
                    print("Resource is not available!")

                break

        if not found:
            print("Resource not found!")

    # 6. Summary Report
    elif choice == "6":

        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("\n--- STUDENT RECORDS ---")

        for sid, name, dept, year in students:
            print(sid, name, dept, year)

        print("\n--- ATTENDANCE DETAILS ---")

        for sid, attended, total, percentage in attendance:
            print(sid, attended, "/", total,
                  "Attendance:", round(percentage, 2), "%")

        print("\n--- MARKS DETAILS ---")

        for record in marks:
            sid, m1, m2, m3, total, average = record

            print(sid, "Total:", total,
                  "Average:", round(average, 2))

        print("\n--- EVENT REGISTRATIONS ---")

        for sid, event in registrations:
            print(sid, "registered for", event)

        print("\n--- RESOURCE AVAILABILITY ---")

        for resource, available in resources:
            print(resource, "Available:", available)

    # 7. Exit
    elif choice == "7":

        print("Exiting Smart Campus Management System.")
        break

    else:

        print("Invalid choice! Please try again.")
