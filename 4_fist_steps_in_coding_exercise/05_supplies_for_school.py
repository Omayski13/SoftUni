pens_pacs = int(input())
markers_pacs = int(input())
litres_cleaner = int(input())
discount_percent = int(input())

price_pens_packs = pens_pacs * 5.80
price_markers_packs = markers_pacs * 7.20
price_litres_cleaner = litres_cleaner * 1.2
total_price_without_discount = price_pens_packs + price_markers_packs + price_litres_cleaner
discount_sum = total_price_without_discount * (discount_percent / 100)
total_price_with_discount = total_price_without_discount - discount_sum

print (total_price_with_discount)
