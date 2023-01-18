first_num = int(input())

sum_numbers = 0

while True:
    inpt_num = int(input())
    sum_numbers += inpt_num


    if sum_numbers >= first_num:
        print(sum_numbers)
        break