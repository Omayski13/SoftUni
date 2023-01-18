product = input()
day = input()
quantity = float(input())

price = 0
flag = True
if day in ['Monday','Tuesday','Wednesday', 'Thursday','Friday']:
    if product == 'banana':
        price = quantity * 2.50
    elif product == 'apple':
        price = quantity * 1.20
    elif product == 'orange':
        price = quantity * 0.85
    elif product == 'grapefruit':
        price = quantity * 1.45
    elif product == 'kiwi':
        price = quantity * 2.70
    elif product == 'pineapple':
        price = quantity * 5.50
    elif product == 'grapes':
        price = quantity * 3.85
    else:
        flag = False

elif day in ['Saturday', 'Sunday']:
    if product == 'banana':
        price = quantity * 2.70
    elif product == 'apple':
        price = quantity * 1.25
    elif product == 'orange':
        price = quantity * 0.90
    elif product == 'grapefruit':
        price = quantity * 1.60
    elif product == 'kiwi':
        price = quantity * 3.00
    elif product == 'pineapple':
        price = quantity * 5.60
    elif product == 'grapes':
        price = quantity * 4.20
    else:
        flag = False
else:
    flag = False


if flag == False:
    print('error')
else:
    print(f'{price:.2f}')