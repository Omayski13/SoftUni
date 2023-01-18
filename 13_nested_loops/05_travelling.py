
destination = input()

money = 0

while destination != 'End':
    needed_money = float(input())
    input_money = float(input())
    while True:
        money += input_money
        if money >= needed_money:
            money = 0
            break
        input_money = float(input())
    print(f"Going to {destination}!")

    destination = input()


