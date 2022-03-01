a = float(input('Enter km for the first day: '))
b = float(input('Enter km: '))
day = 1
print(f"{day}st day: {a} km")
while a < b:
    a += a / 10
    day += 1
    print(f"{day}st day: {a:.2f} km")
print(f"You'll reach the goal in {day} days")