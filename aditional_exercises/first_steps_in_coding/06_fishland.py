price_skumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8

total_price_palamud = kg_palamud * price_palamud
total_price_safrid = kg_safrid * price_safrid
total_price_midi = kg_midi * 7.50
total_price_all = total_price_midi + total_price_safrid + total_price_palamud

print(f"{total_price_all:.2f}")