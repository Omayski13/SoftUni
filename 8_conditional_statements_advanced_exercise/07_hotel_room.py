month = input()
nights = int(input())

price_studio = 0
price_apartament = 0

if month in ['May', 'October']:
    price_studio = nights * 50
    price_apartament = nights * 65
elif month in ['June', 'September']:
    price_studio = nights * 75.20
    price_apartament = nights * 68.70
elif month in ['July', 'August']:
    price_studio = nights * 76
    price_apartament = nights * 77

if nights > 14 and month in ['May', 'October']:
    price_studio *= 0.70
elif nights > 7 and month in ['May', 'October']:
    price_studio *= 0.95
elif nights > 14 and month in ['June', 'September']:
    price_studio *= 0.80

if nights > 14:
    price_apartament *= 0.90

print(f"Apartment: {price_apartament:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")