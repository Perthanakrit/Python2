'''
input distance of both and ความจุของถึงน้ำมัน 

output : 1. 2.

'''

OIL_PER_DISTANCE = 1 / 15

total_distance = int(input())
volume_oil_tank = int(input())

total_used_oil = total_distance * OIL_PER_DISTANCE

kaw_add = int(total_used_oil / (volume_oil_tank * 0.5)) + 1
knew_add = int(total_used_oil / (volume_oil_tank * 0.9)) + 1

print(kaw_add)
print(knew_add)
