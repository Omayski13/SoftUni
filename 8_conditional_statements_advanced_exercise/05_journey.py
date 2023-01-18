budget = float(input())
season = input()

destination = ''
place = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
elif budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if season == 'winter' or destination == 'Europe':
    place ='Hotel'
elif season == 'summer':
    place = 'Camp'


if destination == 'Bulgaria':
    if season == 'summer':
        price = budget * 0.3
    elif season == 'winter':
        price = budget * 0.7
elif destination == 'Balkans':
    if season == 'summer':
        price = budget * 0.4
    elif season == 'winter':
        price = budget * 0.8
elif destination == 'Europe':
    price = budget * 0.9


print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")