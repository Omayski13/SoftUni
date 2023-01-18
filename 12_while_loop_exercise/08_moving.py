lengh = int(input())
width = int(input())
height = int(input())

flag = False
home_size = lengh * width * height
free_space = home_size
count_boxes = 0
input_line = input()

while input_line != 'Done':
    boxes = int(input_line)

    count_boxes += boxes

    if free_space <= count_boxes:
        flag = True
        break

    input_line = input()

diff = abs(free_space - count_boxes)

if flag:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")