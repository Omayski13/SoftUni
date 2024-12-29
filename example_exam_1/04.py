p_1 = input()
p_2 = input()

p_1_points = 0
p_2_points = 0

end_game = False

while True:
    command = input()
    if command == 'End of game':
        end_game = True
        break
    p1_card = int(command)
    p2_card = int(input())

    if p2_card == p1_card:
        print('Number wars!')
        p1_card = int(input())
        p2_card = int(input())
        if p1_card > p2_card:
            print(f"{p_1} is winner with {p_1_points} points")
            break
        else:
            print(f"{p_2} is winner with {p_2_points} points")
            break
    elif p1_card > p2_card:
        p_1_points += p1_card - p2_card
    else:
        p_2_points += p2_card - p1_card

if end_game:
    print(f"{p_1} has {p_1_points} points")
    print(f"{p_2} has {p_2_points} points")

