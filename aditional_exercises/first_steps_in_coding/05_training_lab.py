lenght_w = float(input())
wight_h = float(input())

wight_h_cm = wight_h * 100
lenght_w_cm = lenght_w * 100

wight_without_coridor = wight_h_cm - 100
desk_on_wight= wight_without_coridor // 70
desks_on_lengt = lenght_w_cm // 120

total_desks= desk_on_wight * desks_on_lengt - 3

print(total_desks)