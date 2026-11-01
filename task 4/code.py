
# Nested Loop Calendar Generator

# Input details
month = input("Enter month name: ")

start_day = int(input("Enter starting weekday (0=Mon, 6=Sun): "))

days = int(input("Enter number of days in month: "))

# Validate input
if start_day < 0 or start_day > 6:
    print("Invalid starting weekday!")

elif days not in [28, 29, 30, 31]:
    print("Invalid number of days!")

else:
    print("\n       ", month)
    print("Mon Tue Wed Thu Fri Sat Sun")

    date = 1

    # Outer loop for weeks
    for week in range(6):

        # Inner loop for days
        for day in range(7):

            # Print blank spaces before first date
            if week == 0 and day < start_day:
                print("    ", end="")

            # Print dates
            elif date <= days:
                print("%3d " % date, end="")
                date += 1

            else:
                print("    ", end="")

        print()

        # Stop when all dates are printed
        if date > days:
            break

