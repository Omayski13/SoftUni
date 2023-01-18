hrizantems = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()

price_hrizanteems = 0
price_roses = 0
price_tulips = 0

if season == 'Spring' or season == 'Summer':
    price_hrizanteems = hrizantems * 2
    price_roses = roses * 4.10
    price_tulips = tulips * 2.50
elif season == 'Winter' or season == 'Autumn':
    price_hrizanteems = hrizantems * 3.75
    price_roses = roses * 4.50
    price_tulips = tulips * 4.15

if day == 'Y':
    price_hrizanteems *= 1.15
    price_roses *= 1.15
    price_tulips *= 1.15

price = price_roses + price_tulips + price_hrizanteems

if tulips > 7 and season == 'Spring':
    price *= 0.95

if roses >= 10 and season == "Winter":
    price *= 0.90

if (hrizantems + roses + tulips) > 20:
    price *= 0.80

service = price + 2

print(f'{service:.2f}')