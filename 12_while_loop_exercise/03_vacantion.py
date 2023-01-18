vacantin_cost = float(input())
innit_money = float(input())
spending_days = 0
total_days = 0
total_money = innit_money
flag = False
while total_money < vacantin_cost:
    if spending_days == 5:
        flag = True
        break
    action = input()
    amount = float(input())
    total_days += 1

    if action == 'save':
        total_money += amount
        spending_days = 0

    elif action == 'spend':
        total_money -= amount
        spending_days += 1
        if total_money < 0:
            total_money = 0

if flag:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")

