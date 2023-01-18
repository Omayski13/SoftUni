number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = number * 0.1
else:
    bonus = number * 0.2

aditional_bonus = 0
if number % 2 == 0:
    aditional_bonus = bonus + 1
elif number % 10 == 5:
    aditional_bonus = bonus + 2
else:
    aditional_bonus = bonus

print (aditional_bonus)
print (aditional_bonus + number)


