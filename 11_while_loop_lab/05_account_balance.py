money = 0
while True:
    transfer = input()

    if transfer == 'NoMoreMoney':
        break

    transfer = float(transfer)

    if transfer > 0:
        print(f'Increase: {transfer:.2f}')
        money += transfer
    else:
        print('Invalid operation!')
        break
print(f'Total: {money:.2f}')

