bottles = int(input())



mililiters_soap = bottles * 750
needed_soap = 0
input_line = input()
counter = 0
dishes = 0
pots = 0
flag = False
while input_line != 'End':
    num_dishes = int(input_line)
    counter += 1
    if counter % 3 == 0:
        pots += num_dishes
        needed_soap += num_dishes * 15
    else:
        dishes += num_dishes
        needed_soap += num_dishes * 5

    if needed_soap > mililiters_soap:
        flag = True
        break

    input_line = input()

diff = abs(needed_soap - mililiters_soap)
if flag:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")