'''
    รอบ ค่า i ผลรวม
    1    1    2
    2    2    1+2
    3    3    1+2+3
    4    4    10
    5    5    15
'''

n = 10
i = 1
result = 0

while i <= n:
    result += i
    i = i + 1

print("Done!", result)
