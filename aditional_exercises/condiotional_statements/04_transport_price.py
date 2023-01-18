kilometers = int(input())
time = input()

price = 0
if (time == "day") and (kilometers < 20):
    price = kilometers * 0.79 + 0.70
elif (time == "night") and (kilometers < 20):
    price = kilometers * 0.90 + 0.70
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06

print(f'{price:.2f}')