
# Hospital Ward Occupancy Monitoring

# Input number of wards and days
wards = int(input("Enter number of wards: "))
days = int(input("Enter number of days: "))

ward_names = []
capacities = []
occupancy = []

# Collect ward details
for i in range(wards):

    print("\nWard", i + 1)

    name = input("Enter ward name: ")
    capacity = int(input("Enter total bed capacity: "))

    daily_occupancy = []

    for j in range(days):

        occupied = int(input("Enter occupied beds for Day " + str(j + 1) + ": "))

        daily_occupancy.append(occupied)

    ward_names.append(name)
    capacities.append(capacity)
    occupancy.append(daily_occupancy)

# Calculate utilization and detect violations
print("\n--- HOSPITAL WARD OCCUPANCY REPORT ---")

violations = []

for i in range(wards):

    print("\nWard:", ward_names[i])

    for j in range(days):

        occupied = occupancy[i][j]

        utilization = (occupied / capacities[i]) * 100

        print("Day", j + 1,
              "Occupied Beds:", occupied,
              "Utilization:", round(utilization, 2), "%")

        if occupied > capacities[i]:

            print("WARNING: Capacity Exceeded!")

            violations.append(
                (ward_names[i], j + 1, occupied)
            )

# Calculate total occupancy for each day
daily_totals = []

for j in range(days):

    total = 0

    for i in range(wards):

        total += occupancy[i][j]

    daily_totals.append(total)

# Identify peak-demand day
peak_occupancy = max(daily_totals)
peak_day = daily_totals.index(peak_occupancy) + 1

# Display capacity violations
print("\n--- CAPACITY VIOLATIONS ---")

if len(violations) == 0:

    print("No capacity violations found.")

else:

    for ward, day, count in violations:

        print(ward, "- Day", day,
              "- Occupied Beds:", count)

# Display daily occupancy totals
print("\n--- DAILY TOTAL OCCUPANCY ---")

for j in range(days):

    print("Day", j + 1, ":", daily_totals[j], "beds")

# Display peak demand
print("\n--- PEAK DEMAND ---")

print("Peak Demand Day:", peak_day)
print("Maximum Occupancy:", peak_occupancy, "beds")
