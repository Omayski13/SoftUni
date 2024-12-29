country = input()
item = input()

russia = {
    'ribbon':[9.1,9.4],
    'hoop':[9.3,9.8],
    'rope':[9.6,9.0]
}
bulgaria = {
    'ribbon':[9.6,9.4],
    'hoop':[9.55,9.75],
    'rope':[9.5,9.4]
}
italy = {
    'ribbon':[9.2,9.5],
    'hoop':[9.45,9.35],
    'rope':[9.7,9.15]
}

total_grade = 0

if country == 'Russia':
    total_grade = sum(russia[item])
elif country == 'Bulgaria':
    total_grade = sum(bulgaria[item])
elif country == 'Italy':
    total_grade = sum(italy[item])

percent_num = 20 - total_grade
percent = (percent_num / 20) * 100

print(f"The team of {country} get {total_grade:.3f} on {item}.")
print(f"{percent:.2f}%")

