chicken_menus = int(input())
fish_menus = int(input())
vegetarenian_menus = int(input())

price_chicken_menus = chicken_menus * 10.35
price_fish_menus = fish_menus * 12.40
price_vegetarenian_menus = vegetarenian_menus * 8.15

total_price_menus = price_fish_menus + price_chicken_menus + price_vegetarenian_menus
dessert_price = total_price_menus * (20 / 100)
delivery_price = 2.50

total_price = total_price_menus + dessert_price + delivery_price

print(total_price)

