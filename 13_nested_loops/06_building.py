floors = int(input())
flats = int(input())
counter = 0
type_flat = ''

for i in range(floors, 0, -1):
    for y in range(flats):
        if i == floors:
            type_flat = f'L{i}{y}'
        elif i % 2 == 0:
            type_flat = f'O{i}{y}'
        elif i % 2 != 0:
            type_flat = f'A{i}{y}'

        print(type_flat, end=' ')
    print()

