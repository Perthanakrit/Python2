'''
C D E F G A, B, C#, D
169 / 7 -> 24 * 7 -> 168 
'''

major_scale = input().split(",")
numof_ms = len(major_scale) - 1 
target = int(input())
target = target if target >= 1 else 1

base_index = (target % numof_ms) - 1

print(major_scale[base_index])
