name = input()
failed_years = 0
sum_grades = 0
years = 1

while True:
    grade = float(input())

    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {years} grade")
            break

    elif grade >= 4:
        sum_grades += grade
        years += 1
        if years > 12:
            print(f"{name} graduated. Average grade: {(sum_grades / 12):.2f}")
            break