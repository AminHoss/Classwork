human_year = int(input("How many human years: "))
dog_year = 0
if human_year <= 2:
    dog_year = human_year * 10.5
else:
    dog_year = (human_year - 2) * 4 + 21
print(f"{human_year} human years is equal to {dog_year} dog years")  
