start_interval = int(input())
end_interval = int(input())
magic_num = int(input())
counter = 0
flag = False
for i in range(start_interval, end_interval + 1):
    for y in range(start_interval, end_interval + 1):
        counter += 1

        if i + y == magic_num:
            print(f"Combination N:{counter} ({i} + {y} = {magic_num})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_num}")