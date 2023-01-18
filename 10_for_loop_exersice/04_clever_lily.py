years = int(input())
price_washing_m = float(input())
price_toy = int(input())

even_years = 0
gift_money = 10
money = 0
toys = 0
for i in range (1, years + 1):
    if i % 2 == 0:
        money += gift_money
        gift_money += 10
        even_years += 1
    else:
        toys += 1

money_brother = money - even_years
money_toys = toys * price_toy

total_money = money_toys + money_brother

diff = abs(total_money - price_washing_m)

if total_money >= price_washing_m:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


