time = int(input())
day = input()

if day in ['Monday' ,'Tuesday' ,'Wednesday' , 'Thursday', 'Friday', 'Saturday']:
    if time >= 10 and time <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')