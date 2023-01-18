from math import ceil,floor

x_grapes = int(input())
y_wine = float(input())
z_needed_litres = int(input())
number_workers = int(input())

total_grapes = x_grapes * y_wine
wine = (total_grapes * 0.40) / 2.5

diff = abs(wine - z_needed_litres)
liters_for_workers = ceil(diff / number_workers)
up_diff = ceil(diff)
down_diff = floor(diff)

if wine < z_needed_litres:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {int(wine)} liters.')
    print(f'{ceil(diff)} liters left -> {liters_for_workers} liters per person.')