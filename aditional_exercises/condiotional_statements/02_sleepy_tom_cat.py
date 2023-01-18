holidays = int(input())

working_days = 365 - holidays
holidays_minutes = holidays * 127
working_days_minutes = working_days * 63
total_playing_minutes = working_days_minutes + holidays_minutes


diff = abs(total_playing_minutes - 30000)
hours_playing_hours = diff // 60
playing_minutes = diff % 60

if total_playing_minutes > 30000:
    print('Tom will run away')
    print(f'{hours_playing_hours} hours and {playing_minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours_playing_hours} hours and {playing_minutes} minutes less for play')


