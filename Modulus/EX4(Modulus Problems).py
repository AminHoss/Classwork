total_cents = int(input("The total number of cents: "))
dollars = total_cents // 100
cents= total_cents % 100
print("${:.2f}".format(dollars, cents))
