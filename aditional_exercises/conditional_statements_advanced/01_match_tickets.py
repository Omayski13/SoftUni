budget = float(input())
category = input()
fans = int(input())

price_tickets = 0
if category == 'VIP':
    price_tickets = fans * 499.99
if category == 'Normal':
    price_tickets = fans * 249.99

price_transport = 0
if fans <= 4:
    price_transport = budget * 0.75
elif 4 < fans <= 9:
    price_transport = budget * 0.60
elif 9 < fans <= 24:
    price_transport = budget * 0.50
elif 24 < fans <= 49:
    price_transport = budget * 0.40
elif fans >= 50:
    price_transport = budget * 0.25

price = price_transport + price_tickets
diff = abs(price - budget)

if price < budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


