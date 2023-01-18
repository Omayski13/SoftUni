from math import pi

type = input()
area = 0

if type == 'square':
    a = float(input())
    area = a * a
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif type == 'circle':
    r = float(input())
    area = pi * (r ** 2)
elif type == 'triangle':
    a = float(input())
    b = float(input())
    area = 1/2 * a * b

print(f'{area:.3f}')




