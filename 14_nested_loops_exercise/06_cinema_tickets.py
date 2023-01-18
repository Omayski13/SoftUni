movie = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
flag = False
while movie != 'Finish':
    room_sits = int(input())
    type_ticket = input()
    counter_current_movie = 0
    while type_ticket != 'End':
        if type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'kid':
            kids_tickets += 1
        counter_current_movie += 1
        percent_full = counter_current_movie * (100 / room_sits )
    print(f"{movie} - {percent_full:.2f}% full.")
    counter_current_movie = 0
    type_ticket = input()

    movie = input()
total_tickets = standard_tickets + student_tickets + kids_tickets
percent_standart_tickets = standard_tickets * (100 / total_tickets)
percent_student_tickets = student_tickets * (100 / total_tickets)
percent_kid_tickets = kids_tickets * (100 / total_tickets)
if flag:
    print(f"Total tickets: {total_tickets}")
    print(f"{percent_student_tickets:.2f}% student tickets.")
    print(f"{percent_standart_tickets:.2f}% standard tickets.")
    print(f"{percent_kid_tickets:.2f}% kids tickets.")
