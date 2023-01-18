n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for i in range (1, n + 1):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    elif num >= 800 :
        p5 += 1

total_sum = p1 + p2 + p4 + p4 + p5

p1_percent = p1 * (100 / n)
p2_percent = p2 * (100 / n)
p3_percent = p3 * (100 / n)
p4_percent = p4 * (100 / n)
p5_percent = p5 * (100 / n)

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')