v_pool = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours = float(input())

fuling_first_pipe = first_pipe * hours
fuling_second_pipe = second_pipe * hours

fuling_two_pipes = fuling_second_pipe + fuling_first_pipe
one_percent_fuling_two_pipes= fuling_two_pipes / 100

diff = abs(fuling_two_pipes - v_pool)

percent_first_pipe = fuling_first_pipe / (fuling_two_pipes / 100)
percent_second_pipe = fuling_second_pipe / (fuling_two_pipes / 100)
percent_pool = fuling_two_pipes / (v_pool / 100)

if fuling_two_pipes <= v_pool:
    print(f'The pool is {percent_pool:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.')
else:
    print(f'For {hours:.2f} hours the pool overflows with {diff:.2f} liters.')
