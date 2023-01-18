number_lengt = int(input())

even_count = 0
odd_count = 0

for i in range(1, number_lengt + 1):
    num = int(input())


    if i % 2 == 0:
        even_count += num
    else:
        odd_count += num

diff = abs(even_count - odd_count)

if even_count == odd_count:
    print('Yes')
    print(f'Sum = {even_count}')
else:
    print('No')
    print(f'Diff = {diff}')
