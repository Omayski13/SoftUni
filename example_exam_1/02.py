won = 0
drown = 0
loose = 0


for x in range(3):
    result = input().split(':')
    if int(result[0]) < int(result[1]):
        loose += 1
    elif int(result[0]) > int(result[1]):
        won += 1
    elif int(result[0]) == int(result[1]):
        drown += 1

print(f"Team won {won} games.")
print(f"Team lost {loose} games.")
print(f"Drawn games: {drown}")
