hour_exam = int(input())
minutes_exam = int(input())
hour_arraving = int(input())
minutes_arraving = int(input())

t_m_exam = hour_exam * 60 + minutes_exam
t_m_arraving = hour_arraving * 60 + minutes_arraving
diff = abs(t_m_exam - t_m_arraving)
arraving = ''

if t_m_arraving > t_m_exam:
    arraving = "Late"
elif t_m_arraving < t_m_exam and diff > 30:
    arraving = "Early"
elif t_m_arraving <= t_m_exam and diff <= 30:
    arraving = "On time"

time_minutes= diff % 60
time_hours = diff// 60

print(arraving)
if diff == 0:
    pass
elif arraving == 'On time' or arraving == "Early":
    if diff < 9:
        print(f'{diff} minutes before the start')
    elif diff <= 59:
        print(f'{diff} minutes before the start')
    elif diff > 59 and time_minutes < 9:
        print(f'{time_hours}:0{time_minutes} hours before the start')
    else:
        print(f'{time_hours}:{time_minutes} hours before the start.')
if arraving == 'Late':
    if diff < 9:
        print(f'0{diff} minutes after the start')
    elif diff <= 59:
        print(f'{diff} minutes after the start')
    elif diff > 59 and time_minutes < 9:
        print(f'{time_hours}:0{time_minutes} hours after the start')
    else:
        print(f'{time_hours}:{time_minutes} hours after the start.')

