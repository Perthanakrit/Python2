'''
C D E F G A, B, C#, D
169 / 7 -> 24 * 7 -> 168 
'''
major_scale = input().split(",")
major_scale.pop()
numof_ms = len(major_scale) 
target = int(input()) 
if target > 0:
    target -= 1
    base_index = target - (numof_ms * (target//numof_ms))
    
    print(major_scale[base_index])
'''
21 - 15 = 6
'''
