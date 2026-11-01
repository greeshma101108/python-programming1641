
# Multi-Event Sports Scheduling and Scoring

# Enter event details
n = int(input("Enter number of sports events: "))

events = []

for i in range(n):
    print("\nEvent", i + 1)

    name = input("Enter event name: ")
    date = input("Enter event date (DD-MM-YYYY): ")
    time = input("Enter event time: ")

    # Store event details as a tuple
    events.append((name, date, time))

# Identify scheduling conflicts
print("\n--- SCHEDULING CONFLICT REPORT ---")

conflict_found = False

for i in range(len(events)):
    for j in range(i + 1, len(events)):

        if events[i][1] == events[j][1] and events[i][2] == events[j][2]:
            print("Conflict:", events[i][0], "and", events[j][0])
            conflict_found = True

if not conflict_found:
    print("No scheduling conflicts found.")

# Enter team details
teams = {}

t = int(input("\nEnter number of teams: "))

for i in range(t):
    team_name = input("\nEnter team name: ")

    scores = []

    for event in events:
        score = int(input("Enter score for " + event[0] + ": "))
        scores.append(score)

    # Store team scores
    teams[team_name] = scores

# Calculate total points
total_points = {}

for team, scores in teams.items():
    total_points[team] = sum(scores)

# Sort teams by total points
rankings = sorted(
    total_points.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display event schedule
print("\n--- EVENT SCHEDULE ---")

for event in events:
    print(event[0], "-", event[1], "-", event[2])

# Display final rankings
print("\n--- FINAL TEAM RANKINGS ---")

rank = 0
previous_points = None

for position, (team, points) in enumerate(rankings, start=1):

    if points != previous_points:
        rank = position

    print("Rank:", rank, "| Team:", team, "| Total Points:", points)

    previous_points = points

print("\nSports scheduling and scoring completed.")
