flowers = input()
count_flowers = int(input())
budget = int(input())

price = 0
if flowers == 'Roses':
    price = count_flowers * 5
    if count_flowers > 80:
        price = price * 0.9
elif flowers == 'Dahlias':
    price = count_flowers * 3.80
    if count_flowers > 90:
        price = price * 0.85
elif flowers == 'Tulips':
    price = count_flowers * 2.80
    if count_flowers > 80:
        price = price * 0.85
elif flowers == 'Narcissus':
    price = count_flowers * 3
    if count_flowers < 120:
        price = price * 1.15
elif flowers == 'Gladiolus':
    price = count_flowers * 2.50
    if count_flowers < 80:
        price = price * 1.20

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
