needed_money = int(input())

input_line = input()
counter = 0
money_card = 0
money_cash = 0
card = 0
cash = 0
flag = False
while input_line != 'End':
    transaction = int(input_line)
    counter += 1
    if counter % 2 == 0 :
        if transaction < 10:
            print("Error in transaction!")
        else:
            money_card += transaction
            card += 1
            print('Product sold!')

    else:
        if transaction > 100:
            print("Error in transaction!")
        else:
            money_cash += transaction
            cash += 1
            print('Product sold!')
    total_money = money_cash + money_card
    if total_money >= needed_money:
        flag = True
        break
    input_line = input()

avr_card = money_card / card
avr_cash = money_cash / cash
if flag or total_money >= needed_money:
    print(f"Average CS: {avr_cash:.2f}")
    print(f"Average CC: {avr_card:.2f}")
else:
    print("Failed to collect required money for charity.")