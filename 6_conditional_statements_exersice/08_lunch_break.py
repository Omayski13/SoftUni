from math import ceil

serial_name = input()
episode_lengh = int(input())
lunch_break = int(input())

free_time = lunch_break - ((lunch_break / 8) + (lunch_break / 4))

diff = abs(free_time - episode_lengh)
rounded_diff = ceil(diff)
if free_time >= episode_lengh:
    print(f"You have enough time to watch {serial_name} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded_diff} more minutes.")
