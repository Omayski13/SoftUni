import sys

n = int(input())
total_sum = 0
maxi_num = -sys.maxsize
for i in range(1, n+1):
    num = int(input())
    if num > maxi_num:
        maxi_num = num

        total_sum += num

other_num_sum = total_sum - maxi_num

diff = abs(total_sum - maxi_num)
if other_num_sum == maxi_num:
    print('Yes')
    print(f'Sum = {other_num_sum}')
else:
    print('No')
    print(f'Diff = {diff}')
