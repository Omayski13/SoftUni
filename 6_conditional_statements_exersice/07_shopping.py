budget = float(input())
count_video_carts = int(input())
count_proccesors = int(input())
count_ram = int(input())

price_video_carts = count_video_carts * 250
price_proccesors = count_proccesors * (price_video_carts * 0.35)
price_ram = count_ram * (price_video_carts * 0.10)

total_price = price_ram + price_proccesors + price_video_carts

if count_video_carts > count_proccesors:
    total_price = total_price * 0.85

diff = abs(budget - total_price)


if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
