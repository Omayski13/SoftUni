lengh_cake = int(input())
wight_cake = int(input())
flag = False

cake_size = lengh_cake * wight_cake
input_line = input()
while input_line != 'STOP':
    taken_pieces = int(input_line)
    cake_size -= taken_pieces

    if cake_size <= 0:
        flag = True
        break
    input_line = input()

diff = abs(cake_size)
if flag:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{cake_size} pieces are left.")