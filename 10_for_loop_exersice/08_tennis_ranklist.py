from math import floor

turnirs_count = int(input())
points_ranklist = int(input())


points = 0
wins = 0
for i in range(1, turnirs_count + 1):
    result = input()
    if result == "W":
       points += 2000
       wins += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720
    total_points = points + points_ranklist

percent_wons = wins / turnirs_count * 100
percent_points = points / turnirs_count

print(f'Final points: {total_points}')
print(f"Average points: {floor(percent_points)}")
print(f"{percent_wons:.2f}%")
