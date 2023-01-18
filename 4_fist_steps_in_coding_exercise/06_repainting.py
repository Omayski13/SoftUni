needed_nailon = int(input())
needed_paint = int(input())
needed_razreditel = int(input())
hours_for_work = int(input())

price_for_nailon = (needed_nailon + 2) * 1.50
ten_percent_of_paint = needed_paint * (10/100)
price_for_paint = (needed_paint + ten_percent_of_paint) * 14.50
price_razreditel = needed_razreditel * 5.00
price_bags = 0.40
total_price_materials = price_for_nailon + price_for_paint + price_razreditel + price_bags
percent_workers = total_price_materials * (30 / 100)
price_workers = percent_workers * hours_for_work
total_price_all = total_price_materials + price_workers

print(total_price_all)