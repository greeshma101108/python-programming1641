
# University Examination Result Moderation

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

original_total = 0
moderated_total = 0

subject_results = []

# Process each subject
for i in range(n):

    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")

    maximum = int(input("Enter maximum marks: "))
    original = int(input("Enter original marks: "))
    grace = int(input("Enter moderation marks: "))

    # Validate marks
    if maximum <= 0 or original < 0 or original > maximum or grace < 0 or grace > 5:
        print("Invalid marks or moderation value!")
        continue

    # Apply moderation
    moderated = min(original + grace, maximum)

    # Update totals
    original_total += original
    moderated_total += moderated

    subject_results.append(
        [subject, original, moderated, maximum]
    )

# Calculate maximum total
maximum_total = sum(item[3] for item in subject_results)

if len(subject_results) == 0:
    print("\nNo valid subject records available.")

else:
    # Calculate percentages
    original_percentage = (original_total / maximum_total) * 100

    moderated_percentage = (moderated_total / maximum_total) * 100

    # Check results (35 marks required per subject)
    original_result = all(item[1] >= 35 for item in subject_results)

    moderated_result = all(item[2] >= 35 for item in subject_results)

    # Display report
    print("\n--- EXAMINATION MODERATION REPORT ---")

    print("Student Name:", name)

    print("\nSubject  Original  Moderated  Maximum")

    for item in subject_results:
        print(item[0], "   ", item[1], "       ",
              item[2], "        ", item[3])

    print("\nOriginal Total:", original_total)
    print("Moderated Total:", moderated_total)

    print("Original Percentage:", round(original_percentage, 2), "%")
    print("Moderated Percentage:", round(moderated_percentage, 2), "%")

    print("\nOriginal Result:",
          "PASS" if original_result else "FAIL")

    print("Moderated Result:",
          "PASS" if moderated_result else "FAIL")

    print("Additional Marks:", moderated_total - original_total)
