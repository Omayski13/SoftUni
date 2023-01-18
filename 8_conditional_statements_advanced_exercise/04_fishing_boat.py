budget = int(input())
season = input()
number_fishers = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Winter':
    price = 2600
elif season == 'Summer' or season == 'Autumn':
    price = 4200

if number_fishers <= 6:
    price = price * 0.9
elif 7 < number_fishers <= 11:
    price = price * 0.85
elif number_fishers > 12:
    price = price * 0.75

if season !='Autumn' and number_fishers % 2 == 0:
    price = price * 0.95

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

    # in ['Summer', 'Winter', 'Spring']