type = input()
rows = int(input())
colums = int(input())

income = 0

if type == 'Premiere':
    income = (rows * colums) * 12
elif type == 'Normal':
    income = (rows * colums) * 7.50
elif type == 'Discount':
    income = (rows * colums) * 5

print(f'{income:.2f}')
