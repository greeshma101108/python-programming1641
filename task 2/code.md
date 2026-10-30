
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
