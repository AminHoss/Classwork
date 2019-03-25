total_cents = int(input("The total number of cents: "))
dollars = total_cents // 100
cents= total_cents % 100
toonies = dollars // 2
loonies = dollars % 2
quarters = cents // 25
dimes = cents % 25 // 10
nickels = cents % 250 // 5
pennies = cents % 250 % 5
print("{} toonie(s),{} loonie(s),{} quarter(s),{} dime(s),{} nickel(s), {} pennie(s) and the total cents is ${}.{:>02}".format(toonies, loonies, quarters, dimes, nickels,pennies, dollars, cents))
