junior_riders = int(input())
senior_riders = int(input())
trace = input()

price = 0
if trace == 'trail':
    price = ((junior_riders * 5.50) + (senior_riders * 7)) * 0.95
elif trace == 'cross-country':
    price = ((junior_riders * 8) + (senior_riders * 9.50)) * 0.95
elif trace == 'downhill':
    price = ((junior_riders * 12.25) + (senior_riders * 13.75)) * 0.95
elif trace == 'road':
    price = ((junior_riders * 20) + (senior_riders * 21.50)) * 0.95

if trace == 'cross-country' and (junior_riders + senior_riders) >= 50:
    price *= 0.75

print(f'{price:.2f}')

