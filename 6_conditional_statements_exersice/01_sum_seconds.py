first_time = int(input())
second_time = int(input())
thirt_time = int(input())

sum_all_times = first_time + second_time + thirt_time

minutes = sum_all_times // 60
seconds = sum_all_times % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')