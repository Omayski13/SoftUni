from math import floor

record = float(input())
distance = float(input())
time = float(input())

ivan_time = distance * time
slowing = floor(distance / 15) * 12.5

if (ivan_time + slowing) < record:
    print (f'Yes, he succeeded! The new world record is {ivan_time + slowing:.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivan_time + slowing)- record:.2f} seconds slower.')
