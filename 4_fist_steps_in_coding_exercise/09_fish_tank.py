lenght = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume_aquarium = lenght * width * height
volume_litres = volume_aquarium / 1000
volume_acc = volume_litres * (percent_acc / 100)

needed_lt_water = volume_litres - volume_acc

print (needed_lt_water)