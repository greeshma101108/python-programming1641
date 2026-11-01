### Energy Conservation Before-and-After Analysis – Python Program

Level: B.Tech 1st Year Programming Language: Python

### 1\. Problem Statement

The Energy Conservation Before-and-After Analysis System is designed to compare electricity consumption of different appliances before and after implementing energy-saving methods.

The program accepts the following details:

* Number of appliances.

* Appliance name.

* Electricity usage before intervention (in kWh).

* Electricity usage after intervention (in kWh).

The system performs the following operations:

* Calculates electricity savings for each appliance.

* Calculates savings percentage.

* Identifies appliances with the highest energy savings.

* Ranks appliances according to their achieved savings.

* Displays the results in descending order.

Formula:

Electricity Saved:

\\text{Saved}=\\text{Before Usage}-\\text{After Usage}

Savings Percentage:

\\text{Savings \\%}=
\\frac{\\text{Before}-\\text{After}}{\\text{Before}}\\times100

### 2\. Algorithm

* Start the program.

* Enter the number of appliances.

* Create an empty list to store appliance details.

* Enter the appliance name.

* Enter electricity consumption before intervention.

* Enter electricity consumption after intervention.

* Check whether the entered electricity values are valid.

* Calculate electricity saved for each appliance.

* Calculate savings percentage using the formula.

* Store the appliance details and calculated savings.

* Repeat the process for all appliances.

* Sort appliances according to savings percentage in descending order.

* Assign ranks to appliances.

* Display appliance name, before usage, after usage, electricity saved and savings percentage.

* Stop the program.

### 3\. Flowchart

START

Enter number of appliances

Enter appliance name and electricity usage

Calculate electricity saved

Calculate savings percentage

Store appliance details

Are all appliances entered?

No → Enter next appliance; Yes → Continue

Sort appliances by savings percentage

Display ranked results

STOP


### 4\. Python Source Code

```python

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
```

### 5\. Sample Input

```text
Enter number of appliances: 3

Appliance 1
Enter appliance name: Fan
Enter usage before intervention (kWh): 100
Enter usage after intervention (kWh): 60

Appliance 2
Enter appliance name: Light
Enter usage before intervention (kWh): 80
Enter usage after intervention (kWh): 40

Appliance 3
Enter appliance name: AC
Enter usage before intervention (kWh): 200
Enter usage after intervention (kWh): 150
```

### 6\. Sample Output

```text
--- ENERGY CONSERVATION REPORT ---

Rank  Appliance  Before  After  Saved  Savings %

1     Light      80      40     40     50.0 %
2     Fan        100     60     40     40.0 %
3     AC         200     150    50     25.0 %

Highest Savings Appliance: Light
```

### 7\. Conclusion

The Energy Conservation Before-and-After Analysis System compares electricity consumption before and after energy-saving interventions. It calculates electricity savings, determines savings percentages and ranks appliances based on their performance.

This program helps identify which appliances have achieved the highest percentage of energy savings.

Python concepts used:

* Variables and data types

* Lists

* `for` loops

* Conditional statements

* Arithmetic operators

* `sort()` function

* `lambda` function

* `enumerate()` function

* `round()` function

Suitable for B.Tech 1st Year Practical Record

Note: Electricity consumption is measured in kWh (kilowatt-hours). A negative saving percentage means electricity usage increased after the intervention.

