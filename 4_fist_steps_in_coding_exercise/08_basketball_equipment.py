annual_price = int(input())

percent_shoes = annual_price * (40 / 100)
price_shoes = annual_price - percent_shoes
percent_kit = price_shoes * (20 / 100)
price_kit = price_shoes - percent_kit
percent_ball = price_kit * (75 / 100)
price_ball = price_kit - percent_ball
percent_acc = price_ball * (80 / 100)
price_acc = price_ball - percent_acc

total_price = annual_price + price_shoes + price_kit + price_ball + price_acc

print(total_price)
