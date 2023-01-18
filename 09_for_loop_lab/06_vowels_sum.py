text = input()

sum = 0
for char in range(0, len(text)):
    if text[char] == 'a':
        sum += 1
    if text[char] == 'e':
        sum += 2
    if text[char] == 'o':
        sum += 4
    if text[char] == 'u':
        sum += 5
    if text[char] == 'i':
        sum += 3

print(sum)