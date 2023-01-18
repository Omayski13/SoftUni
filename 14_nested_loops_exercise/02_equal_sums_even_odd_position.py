start_num = int(input())
end_num = int(input())

even_sum = 0
odd_sum = 0
for number in range(start_num, end_num + 1):
    number_to_str = str(number)

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        if index % 2 != 0:
            odd_sum += int(digit)

        if even_sum == odd_sum:
            print(number, end=' ')