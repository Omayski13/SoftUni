hour_exam = int(input())
minutes_exam = int(input())
hour_arriving = int(input())
minutes_arriving = int(input())

total_m_exam = hour_exam * 60 + minutes_exam
total_m_arriving = hour_arriving * 60 + minutes_arriving

diff = abs(total_m_arriving - total_m_exam)
hours = diff // 60
minutes = diff % 60


if total_m_arriving > total_m_exam:
    print('Late')
    if diff <= 59:
        print(f'{minutes} minutes after the start')
    elif hours >= 1 and minutes <= 9:
        print(f'{hours}:0{minutes} hours after the start')
    elif hours >= 1 and minutes > 9:
        print(f'{hours}:{minutes} hours after the start')
elif total_m_arriving < total_m_exam and diff <= 30:
    print('On time')
    print(f'{minutes} minutes before the start')
elif total_m_arriving == total_m_exam:
    print('On time')
elif total_m_arriving < total_m_exam and diff > 30:
    print('Early')
    if diff < 59:
        print(f'{minutes} minutes before the start')
    elif hours >=1 and minutes <= 9:
        print(f'{hours}:0{minutes} hours before the start')
    elif hours >=1 and minutes > 9:
        print(f'{hours}:{minutes} hours before the start')