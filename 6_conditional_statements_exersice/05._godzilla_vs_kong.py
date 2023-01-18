budget = float(input())
people = int(input())
price_clothing_per_pers = float(input())

decor_price = budget * 0.1
clothing_price = people * price_clothing_per_pers

if people > 150:
    clothing_price = clothing_price - (clothing_price * 0.1)

total_price = decor_price + clothing_price

if total_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {(total_price - budget):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {(budget - total_price):.2f} leva left.')


