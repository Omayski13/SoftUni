innit_hour =int(input())
innit_minutes =int(input())

total_minutes = (innit_hour * 60) + innit_minutes + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')


