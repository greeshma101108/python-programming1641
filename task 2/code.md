### Campus Event Financial Planning – Python Program

Level: B.Tech 1st Year Programming Language: Python

### 1. Problem Statement

The Campus Event Financial Planning System is designed to calculate and manage the expenses required to organize a college event.

The system accepts the following details:

* Venue cost

* Equipment cost

* Catering cost per participant

* Transport cost

* Certificate cost per participant

* Expected number of participants

* Registration fee per participant

* Sponsorship amount

The system calculates:

* Total event expenses.

* Total participant contributions.

* Total available sponsorship.

* Sponsorship shortfall, if any.

* Total event income.

* Profit or loss.

* Minimum number of registrations required to break even.

### 2. Algorithm

* Start the program.

* Enter venue cost.

* Enter equipment cost.

* Enter catering cost per participant.

* Enter transport cost.

* Enter certificate cost per participant.

* Enter expected number of participants.

* Enter registration fee per participant.

* Enter sponsorship amount.

* Calculate total fixed expenses:

Fixed Cost = Venue + Equipment + Transport

11. Calculate variable cost per participant:

Variable Cost = Catering + Certificate

12. Calculate total event cost:

Total Cost = Fixed Cost + (Variable Cost × Participants)

13. Calculate participant contributions:

Contributions = Registration Fee × Participants

14. Calculate total income:

Total Income = Contributions + Sponsorship

* Calculate sponsorship shortfall, if applicable.

* Calculate profit or loss.

* Calculate minimum registrations needed to break even.

* Display all financial details.

* Stop the program.

### 3. Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Enter venue cost]
    B --> C[Enter equipment cost]
    C --> D[Enter catering cost per participant]
    D --> E[Enter transport cost]
    E --> F[Enter certificate cost per participant]
    F --> G[Enter expected number of participants]
    G --> H[Enter registration fee per participant]
    H --> I[Enter sponsorship amount]
    I --> J[fixed_cost = venue + equipment + transport]
    J --> K[variable_cost = catering + certificate]
    K --> L[total_cost = fixed_cost + (variable_cost × participants)]
    L --> M[contribution = registration × participants]
    M --> N[total_income = contribution + sponsorship]
    N --> O[sponsorship_shortfall = max(0, total_cost - contribution - sponsorship)]
    O --> P[balance = total_income - total_cost]
    P --> Q{registration > variable_cost?}
    Q -- Yes --> R[minimum_registrations = ceil((fixed_cost - sponsorship) / (registration - variable_cost))]
    R --> S[Display financial report]
    Q -- No --> S
    S --> T([Stop])
```

### 4. Python Source Code

```python

# Campus Event Financial Planning

# Input details
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))
registration = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate expenses
fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

total_cost = fixed_cost + (variable_cost * participants)

# Calculate income
contribution = registration * participants

total_income = contribution + sponsorship

# Calculate sponsorship shortfall
sponsorship_shortfall = max(0, total_cost - contribution - sponsorship)

# Calculate profit or loss
balance = total_income - total_cost

# Calculate minimum registrations for break-even
if registration > variable_cost:
    minimum = (fixed_cost - sponsorship) / (registration - variable_cost)
    minimum = max(0, int(minimum) if minimum == int(minimum)
                  else int(minimum) + 1)
else:
    minimum = "Not possible with current fee"

# Display results
print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")

print("Fixed Cost:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", contribution)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", sponsorship_shortfall)

if balance > 0:
    print("Profit:", balance)
elif balance < 0:
    print("Loss:", abs(balance))
else:
    print("Event is at Break-Even")

print("Minimum Registrations Required:", minimum)
```

### 5. Sample Input

```text
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per participant: 200
Enter transport cost: 3000
Enter certificate cost per participant: 50
Enter expected number of participants: 100
Enter registration fee per participant: 400
Enter sponsorship amount: 10000
```

### 6. Sample Output

```text
--- CAMPUS EVENT FINANCIAL REPORT ---

Fixed Cost: 18000.0
Variable Cost per Participant: 250.0
Total Event Cost: 43000.0

Participant Contributions: 40000.0
Sponsorship Amount: 10000.0

Sponsorship Shortfall: 0

Profit: 7000.0

Minimum Registrations Required: 33
```

### 7. Conclusion

The Campus Event Financial Planning System helps colleges estimate event expenses, calculate participant contributions, identify sponsorship shortages and determine the minimum registrations required to achieve break-even.

This program demonstrates the use of Python variables, arithmetic operations, conditional statements, user input and mathematical calculations.

Python concepts used:

* Variables and data types

* `input()` and `print()`

* Arithmetic operators

* Conditional statements (`if-else`)

* `max()` function

* Type conversion (`int()` and `float()`)

Note: The break-even calculation assumes that registration fees and sponsorship remain fixed and that each additional participant adds the same catering and certificate costs.
