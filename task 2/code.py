
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

