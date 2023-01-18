num_jury = int(input())
presentation = input()
sum_all_grades = 0
counter = 0

while presentation != 'Finish':
    sum_grades = 0
    for i in range(1, num_jury + 1):
        grade = float(input())
        sum_grades += grade
        sum_all_grades += grade
        counter += 1
        avr_grade = sum_grades / num_jury

    print(f"{presentation} - {avr_grade:.2f}.")

    presentation = input()
avr_grade_all = sum_all_grades / counter
print(f"Student's final assessment is {avr_grade_all:.2f}.")