from math import floor

tournaments = int(input())

inital_points = int(input())
won_points = 0
won_tournaments = 0

for i in range(0,tournaments):
    outcome = input()
    if outcome == 'W':
        won_points += 2000
        won_tournaments += 1
    elif outcome == 'F':
        won_points += 1200
    else:
        won_points += 720

print(f"Final points: {won_points + inital_points}")
print(f"Average points: {floor(won_points / tournaments)}")
print(f'{(won_tournaments/ tournaments) * 100:.2f}%')



