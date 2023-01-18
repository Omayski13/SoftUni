
num = int(input())
counter = 0
for i in range(num + 1):
    for y in range(num + 1):
       for g in range (num + 1):

           if i + y + g == num:
               counter += 1





print(counter)