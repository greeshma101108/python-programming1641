
# Password Policy Validation Engine

password = input("Enter your password: ")

errors = []

# Rule 1: Minimum length
if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

# Rule 2: Uppercase letter
if not any(ch.isupper() for ch in password):
    errors.append("Password must contain an uppercase letter.")

# Rule 3: Lowercase letter
if not any(ch.islower() for ch in password):
    errors.append("Password must contain a lowercase letter.")

# Rule 4: Digit
if not any(ch.isdigit() for ch in password):
    errors.append("Password must contain at least one digit.")

# Rule 5: Special character
if not any(not ch.isalnum() for ch in password):
    errors.append("Password must contain a special character.")

# Rule 6: Repeated characters
repeated = False

for i in range(len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        repeated = True
        break

if repeated:
    errors.append("Password must not contain 3 consecutive identical characters.")

# Rule 7: Prohibited substrings
prohibited = ["password", "admin", "123456"]

for word in prohibited:
    if word in password.lower():
        errors.append("Password contains a prohibited substring: " + word)

# Display result
print("\n--- PASSWORD VALIDATION RESULT ---")

if len(errors) == 0:
    print("Password is Valid!")
else:
    print("Password is Invalid.")
    print("\nFailed Conditions:")

    for error in errors:
        print("-", error)

