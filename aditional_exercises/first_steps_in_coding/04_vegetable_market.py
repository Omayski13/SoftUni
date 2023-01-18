price_for_kg_vegetables = float(input())
price_for_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total_price_vegetables = price_for_kg_vegetables * total_kg_vegetables
total_price_fruits = price_for_kg_fruits * total_kg_fruits

total_price_all = total_price_fruits + total_price_vegetables
total_price_all_euro = total_price_all / 1.94

print(f"{total_price_all_euro:.2f}")


