days = int(input())
room = input()
degree = input()

price = 0
if room == 'apartment':
    if days < 10:
        price = ((days - 1) * 25) * 0.70
    elif 10 <= days < 15:
        price = ((days - 1) * 25) * 0.65
    elif days > 15:
        price = ((days - 1) * 25) * 0.50
if room == 'president apartment':
    if days < 10:
        price = ((days - 1) * 35) * 0.90
    elif 10 >= days < 15:
        price = ((days - 1) * 35) * 0.85
    elif days > 15:
        price = ((days - 1) * 35) * 0.80
if room == 'room for one person':
    price = (days - 1) * 18


if degree == 'positive':
    price = price + (price * 0.25)
if degree == 'negative':
    price = price - (price * 0.10)

print(f'{price:.2f}')
