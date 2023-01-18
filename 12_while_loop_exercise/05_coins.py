
money = float(input())

coins = money * 100

two_coins = coins // 200
coins %= 200
one_coins = coins // 100
coins = coins % 100
fifty_coins = coins // 50
coins %= 50
twelve_coins = coins // 20
coins %= 20
ten_coins = coins // 10
coins %= 10
five_coins = coins // 5
coins %= 5
zero_two_coins = coins // 2
coins %= 2
zero_one_coins = coins // 1

sum_coins = two_coins + one_coins + fifty_coins + twelve_coins + ten_coins + five_coins +\
            zero_one_coins + zero_two_coins


print(f'{sum_coins:.0f}')