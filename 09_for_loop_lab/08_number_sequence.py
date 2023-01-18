import sys

number_lenght = int(input())
maxi_number = -sys.maxsize
min_number = sys.maxsize
for i in range(number_lenght):
    number = int(input())

    if number > maxi_number:
        maxi_number = number
    if number < min_number:
        min_number = number

print(f'Max number: {maxi_number}')
print(f'Min number: {min_number}')