work_start = int(input("What hour do you start working?"))
work_end = int(input("What hour does work end?"))
exercise_goal = int(input("how many hours per day do you want to exercise?"))
screentime_limit = int(input("How many hours (apart from work hours) do you want to limit your screen time to?"))
screentime = 0
exercise_hours = 0
i = 0
hours = []
for i in range(24):
    hours.append(input())
while i < len(hours):
    hour = hours[i]
    if work_start > i or work_end < i:
        if hour == "Onscreen":
            screentime += 1
        if hour == "Exercise":
            exercise_hours += 1
    i += 1
print(screentime)
if screentime > screentime_limit:
    print("You played too much")
    print(f"You're {(screentime // screentime_limit) ** 100} there!")
