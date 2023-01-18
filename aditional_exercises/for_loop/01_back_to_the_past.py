legacy_money = float(input())
year_to_live = int(input())


money = legacy_money
ivan_years = 17
for i in range(1800, year_to_live + 1):
    ivan_years += 1
    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + (ivan_years * 50)

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")