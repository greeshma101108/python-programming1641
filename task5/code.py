
# Energy Conservation Before-and-After Analysis

appliances = []

n = int(input("Enter number of appliances: "))

# Get appliance details
for i in range(n):

    print("\nAppliance", i + 1)

    name = input("Enter appliance name: ")

    before = float(input("Enter usage before intervention (kWh): "))

    after = float(input("Enter usage after intervention (kWh): "))

    # Validate electricity usage
    if before <= 0 or after < 0:
        print("Invalid electricity usage!")
        continue

    # Calculate savings
    saved = before - after

    percentage = (saved / before) * 100

    # Store appliance details
    appliances.append([name, before, after, saved, percentage])

# Sort based on savings percentage
appliances.sort(key=lambda x: x[4], reverse=True)

# Display results
print("\n--- ENERGY CONSERVATION REPORT ---")

print("Rank  Appliance  Before  After  Saved  Savings %")

for rank, item in enumerate(appliances, 1):

    print(rank, "   ", item[0], "   ",
          item[1], "   ", item[2], "   ",
          item[3], "   ", round(item[4], 2), "%")

# Display best performing appliance
if len(appliances) > 0:
    print("\nHighest Savings Appliance:", appliances[0][0])
else:
    print("\nNo valid appliance records available.")

