work_start = int(input("What hour do you start working? "))
work_end = int(input("What hour does work end? "))
exercise_goal = int(input("how many hours per day do you want to exercise? "))
screen_limit = int(input("How many hours (apart from work hours) do you want to limit your screen time to? "))
hours = []
screen_time = 0
exercise = 0

for i in range(1, 25):
    if not work_start <= i <= work_end:
        hours.append(input("{}:00: ".format(i)))
for i in hours:
    if i == "1":
        screen_time += 1
    if i == "2":
        exercise += 1
print(screen_time)
print(exercise)
if screen_time > screen_limit:
    print("You spent too much time onscreen!")
    screen_progress = screen_limit / screen_time * 100
    print("You are {}% of the way there.".format(screen_progress))
if exercise_goal > exercise:
    print("You didn't spend enough time exercising!")
    ex_progress = exercise / exercise_goal * 100
    print("You are {}% of the way there.".format(ex_progress))

