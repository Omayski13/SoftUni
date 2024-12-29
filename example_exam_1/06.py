wanted_height = int(input())

jumps = 0
tries = 0
letva_height = wanted_height - 30
while True:

    jump = int(input())
    jumps += 1
    if jump > letva_height:
        if letva_height < wanted_height:
            letva_height += 5
            tries = 0
        else:
            print(f"Tihomir succeeded, he jumped over {letva_height}cm after {jumps} jumps.")
            break
    else:
        tries += 1
        if tries == 3:
            print(f"Tihomir failed at {letva_height}cm after {jumps} jumps.")
            break

