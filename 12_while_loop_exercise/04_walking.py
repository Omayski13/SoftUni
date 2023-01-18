flag= False
total_steps = 0
input_line = input()

while input_line != 'Going home':
    curent_steps = int(input_line)
    total_steps += curent_steps

    if total_steps > 10000:
        frag = True
        break

    input_line = input()

if input_line == 'Going home':
    home_steps = int(input())
    total_steps += home_steps

diff = abs(total_steps - 10000)

if flag or total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif total_steps < 10000:
    print(f"{diff} more steps to reach goal.")