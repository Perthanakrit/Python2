'''
( damage per enemy) 
3
3 6 3 12 63 3
10
25 92 64
'''
import math

damage_per_bullet = int(input())
hp_list = [int(x) for x in input().split()]
total_used_bullets = 0
bullet_lst = []

for hp in hp_list:
    total_used_bullets += math.ceil(hp / damage_per_bullet)
    bullet_lst.append(str(total_used_bullets))

print(total_used_bullets)
if len(bullet_lst) > 0:
    print(" ".join(bullet_lst))
