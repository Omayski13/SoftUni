# poor_grades = int(input())
# sum_grades = 0
# succes_problems = 0
# failed_problems = 0
#
# proble_name = ''
# has_failed = True
#
# while failed_problems < poor_grades:
#     name_proble = input()
#     if name_proble == 'Enough':
#         has_failed = False
#         break
#
#     grade = int(input())
#     if grade <= 4:
#         failed_problems += 1
#     sum_grades += grade
#     proble_name = name_proble
#     if has_failed:
#             print(f"You need a break, {poor_grades} poor grades.")
#             break
#     else:
#         print(f"Average score: {(sum_grades/ count_problems):.2f}")
#         print(f"Number of problems: {count_problems}")
#         print(f"Last problem: {proble_name}")



poor_grades = int(input())
fails = 0
num_problems = 0
last_problem = ''
sum_grades = 0
flag = False
while fails < poor_grades:
    current_problem = input()
    if current_problem == "Enough":
        flag = True
        break

    grade = int(input())
    num_problems += 1
    last_problem = current_problem
    sum_grades += grade
    if grade <= 4:
        fails += 1

if flag:
    avr_grade = sum_grades / num_problems
    print(f"Average score: {avr_grade:.2f}")
    print(f"Number of problems: {num_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f'You need a break, {poor_grades} poor grades.')






