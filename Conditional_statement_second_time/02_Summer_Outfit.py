degree = int(input())
time = input()
outfit = ''
shoes = ''

if 10 <= degree <= 18:
    if time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    if time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degree <= 24:
    if time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degree >= 25:
    if time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")