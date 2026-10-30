### Multi-Currency Travel Budget Analysis – Python Program

### 1\. Problem Statement

The Multi-Currency Travel Budget Analysis system is designed to calculate and analyse travel expenses in different currencies.

The program accepts travel expenses in multiple currencies and converts them into a single base currency using the supplied exchange rates. It also incorporates currency conversion fees, calculates the total travel expenditure, compares the total expenditure with the planned budget, and identifies the largest expense category.

The system displays the converted expenses, total spending, remaining budget or excess amount, and the largest expense category.

### 2\. Algorithm

Step 1: Start the program.

Step 2: Read the planned travel budget in the base currency (INR).

Step 3: Read the number of expense categories.

Step 4: For each expense category, input:

* Category name.

* Expense amount.

* Currency code.

* Exchange rate.

* Conversion fee percentage.

Step 5: Convert each expense into the base currency using the formula:

\\text{Converted Amount}=\\text{Amount}\\times\\text{Exchange Rate}

Step 6: Calculate the conversion fee.

\\text{Fee}=\\frac{\\text{Converted Amount}\\times\\text{Fee \\%}}{100}

Step 7: Calculate the total expense including the conversion fee.

\\text{Total}=\\text{Converted Amount}+\\text{Fee}

Step 8: Add all expenses to calculate the total travel expenditure.

Step 9: Compare total expenditure with the planned budget.

* If total expenditure is less than the budget, calculate the remaining balance.

* If total expenditure is greater than the budget, calculate the excess amount.

* Otherwise, display that the budget is exactly used.

Step 10: Identify the largest expense category.

Step 11: Display the complete expense report.

Step 12: Stop the program.

### 3\. Flowchart

START

Input planned budget and number of expenses

Input category, amount, currency, exchange rate and fee

Convert expense into INR and calculate fee

Calculate total expense and find largest category

Compare total spending with budget

Display expense report and budget status

STOP

### 4\. Python Source Code

```python

# Multi-Currency Travel Budget Analysis

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

# Input planned budget
budget = float(input("Enter planned budget in INR: "))

# Input number of expense categories
n = int(input("Enter number of expense categories: "))

total_expense = 0
expenses = {}

# Process each expense
for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ")

    rate = float(input("Enter exchange rate to INR: "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    # Currency conversion
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * fee_percent / 100

    # Total expense including fee
    final_amount = converted_amount + fee

    expenses[category] = final_amount
    total_expense += final_amount

    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Final Expense: Rs.", round(final_amount, 2))

# Calculate largest expense category
largest_category = max(expenses, key=expenses.get)

# Compare budget
print("\n========== TRAVEL EXPENSE REPORT ==========")

print("Planned Budget: Rs.", round(budget, 2))
print("Total Expenditure: Rs.", round(total_expense, 2))

if total_expense < budget:
    remaining = budget - total_expense
    print("Budget Status: Within Budget")
    print("Remaining Budget: Rs.", round(remaining, 2))

elif total_expense > budget:
    excess = total_expense - budget
    print("Budget Status: Over Budget")
    print("Excess Amount: Rs.", round(excess, 2))

else:
    print("Budget Status: Budget Fully Used")

print("\nLargest Expense Category:", largest_category)
print("Largest Expense Amount: Rs.",
      round(expenses[largest_category], 2))

print("\n========== END OF REPORT ==========")
```

### 5\. Sample Input

EXAMPLE INPUT VALUES

```text
Enter planned budget in INR: 100000
Enter number of expense categories: 4

Expense 1
Enter expense category: Accommodation
Enter expense amount: 300
Enter currency code: USD
Enter exchange rate to INR: 85
Enter conversion fee percentage: 2

Expense 2
Enter expense category: Food
Enter expense amount: 200
Enter currency code: EUR
Enter exchange rate to INR: 90
Enter conversion fee percentage: 2

Expense 3
Enter expense category: Transport
Enter expense amount: 100
Enter currency code: USD
Enter exchange rate to INR: 85
Enter conversion fee percentage: 1

Expense 4
Enter expense category: Shopping
Enter expense amount: 150
Enter currency code: GBP
Enter exchange rate to INR: 110
Enter conversion fee percentage: 2
```

### 6\. Sample Output

```text
MULTI-CURRENCY TRAVEL BUDGET ANALYSIS

Expense 1
Converted Amount: Rs. 25500.00
Conversion Fee: Rs. 510.00
Final Expense: Rs. 26010.00

Expense 2
Converted Amount: Rs. 18000.00
Conversion Fee: Rs. 360.00
Final Expense: Rs. 18360.00

Expense 3
Converted Amount: Rs. 8500.00
Conversion Fee: Rs. 85.00
Final Expense: Rs. 8585.00

Expense 4
Converted Amount: Rs. 16500.00
Conversion Fee: Rs. 330.00
Final Expense: Rs. 16830.00

========== TRAVEL EXPENSE REPORT ==========

Planned Budget: Rs. 100000.00
Total Expenditure: Rs. 69785.00

Budget Status: Within Budget
Remaining Budget: Rs. 30215.00

Largest Expense Category: Accommodation
Largest Expense Amount: Rs. 26010.00

========== END OF REPORT ==========
```

### 7\. Result

The Multi-Currency Travel Budget Analysis program was successfully implemented using Python.

The program converts expenses from different currencies into Indian Rupees (INR), calculates conversion fees, determines total expenditure, compares spending with the planned budget, and identifies the largest expense category.

Program completed successfully

Note: Exchange rates in this example are assumed values for demonstrating the program. In a real application, current exchange rates should be supplied.
