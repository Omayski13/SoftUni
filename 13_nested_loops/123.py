
movie = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
seats_taken = 0

while movie != 'Finish':
    seats = int(input())
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
        seats_taken += 1
        if seats <= seats_taken:
            break
        ticket_type = input()
    print(f'{movie} - {(seats_taken / seats * 100):.2f}% full.')
    seats_taken = 0
    movie = input()

total_tickets = standard_tickets + student_tickets + kid_tickets

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets * 100):.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets * 100):.2f}% kids tickets.')