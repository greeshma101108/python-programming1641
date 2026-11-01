
# Environmental Monitoring Data Analyzer

# Input number of locations
n = int(input("Enter number of monitoring locations: "))

# Initialize nested list
locations = []
all_readings = []

# Collect environmental readings
for i in range(n):

    print("\nLocation", i + 1)

    name = input("Enter location name: ")

    count = int(input("Enter number of readings: "))

    readings = []

    for j in range(count):

        value = float(input("Enter AQI reading: "))

        readings.append(value)
        all_readings.append(value)

    locations.append([name, readings])

# Analyze environmental data
print("\n--- ENVIRONMENTAL MONITORING REPORT ---")

for location in locations:

    name = location[0]
    readings = location[1]

    average = sum(readings) / len(readings)

    minimum = min(readings)
    maximum = max(readings)

    print("\nLocation:", name)
    print("Readings:", readings)
    print("Average AQI:", round(average, 2))
    print("Minimum AQI:", minimum)
    print("Maximum AQI:", maximum)

    print("Classification:")

    for value in readings:

        if value <= 50:
            category = "Good"

        elif value <= 100:
            category = "Moderate"

        else:
            category = "Poor"

        print(value, "-", category)

# Overall analysis
overall_average = sum(all_readings) / len(all_readings)

overall_minimum = min(all_readings)
overall_maximum = max(all_readings)

print("\n--- OVERALL ENVIRONMENTAL SUMMARY ---")

print("Overall Average AQI:", round(overall_average, 2))
print("Overall Minimum AQI:", overall_minimum)
print("Overall Maximum AQI:", overall_maximum)

print("\nEnvironmental Analysis Completed.")

# Environmental Monitoring Data Analyzer

# Input number of locations
n = int(input("Enter number of monitoring locations: "))

# Initialize nested list
locations = []
all_readings = []

# Collect environmental readings
for i in range(n):

    print("\nLocation", i + 1)

    name = input("Enter location name: ")

    count = int(input("Enter number of readings: "))

    readings = []

    for j in range(count):

        value = float(input("Enter AQI reading: "))

        readings.append(value)
        all_readings.append(value)

    locations.append([name, readings])

# Analyze environmental data
print("\n--- ENVIRONMENTAL MONITORING REPORT ---")

for location in locations:

    name = location[0]
    readings = location[1]

    average = sum(readings) / len(readings)

    minimum = min(readings)
    maximum = max(readings)

    print("\nLocation:", name)
    print("Readings:", readings)
    print("Average AQI:", round(average, 2))
    print("Minimum AQI:", minimum)
    print("Maximum AQI:", maximum)

    print("Classification:")

    for value in readings:

        if value <= 50:
            category = "Good"

        elif value <= 100:
            category = "Moderate"

        else:
            category = "Poor"

        print(value, "-", category)

# Overall analysis
overall_average = sum(all_readings) / len(all_readings)

overall_minimum = min(all_readings)
overall_maximum = max(all_readings)

print("\n--- OVERALL ENVIRONMENTAL SUMMARY ---")

print("Overall Average AQI:", round(overall_average, 2))
print("Overall Minimum AQI:", overall_minimum)
print("Overall Maximum AQI:", overall_maximum)

print("\nEnvironmental Analysis Completed.")
