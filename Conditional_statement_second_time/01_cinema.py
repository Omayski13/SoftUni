ticket = input()
rows = int(input())
colums = int(input())

price = 0
seats = rows * colums

if ticket == 'Premiere':
    price = 12
elif ticket == 'Normal':
    price = 7.5
elif ticket == 'Discount':
    price = 5

outcome = seats * price

print(f'{outcome:.2f} leva.')


