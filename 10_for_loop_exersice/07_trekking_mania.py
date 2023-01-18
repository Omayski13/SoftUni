number_groups = int(input())

mussala = 0
mon_blant = 0
kilimandjaro = 0
k2 = 0
everest = 0
count_people = 0
for i in range(1, number_groups + 1):
    people = int(input())
    count_people += people
    if people <= 5:
        mussala += people
    elif 5 < people <= 12:
        mon_blant += people
    elif 12 < people <= 25:
        kilimandjaro += people
    elif 25 < people <= 40:
        k2 += people
    elif people > 40:
        everest += people

percent_mussala = mussala / count_people * 100
percent_mont_blant = mon_blant / count_people * 100
percent_kilimandjaro = kilimandjaro / count_people * 100
percent_k2 = k2 / count_people * 100
percent_everest = everest / count_people * 100

print(f'{percent_mussala:.2f}%')
print(f'{percent_mont_blant:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
