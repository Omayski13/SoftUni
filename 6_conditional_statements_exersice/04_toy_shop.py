excursion_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

count_all_toys = number_trucks + number_bears + number_dolls + number_minions + number_puzzles

price = (number_trucks * 2) + (number_bears * 4.1) + (number_dolls * 3) + (number_minions * 8.2) + (number_puzzles *2.6)

if count_all_toys >= 50:
    price = price - (price * 0.25)

money_total = price - (price * 0.1)

if money_total < excursion_price:
    print(f'Not enough money! {(excursion_price - money_total):.2f} lv needed.')
else:
    print(f'Yes! {(money_total - excursion_price):.2f} lv left.')



