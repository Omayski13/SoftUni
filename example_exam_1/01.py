from math import floor, ceil

price_per_rocket = int(input())
count_rockets = int(input())
count_trainers = int(input())

price_per_trainers = price_per_rocket / 6

price_rockets = count_rockets * price_per_rocket
price_trainers = count_trainers * price_per_trainers
additional_counts = (price_rockets + price_trainers) * 0.2

total_price = price_rockets + price_trainers + additional_counts

djokovic_price = total_price / 8

total_price -= djokovic_price

print(f"Price to be paid by Djokovic {floor(djokovic_price)}")
print(f"Price to be paid by sponsors {ceil(total_price)}")


