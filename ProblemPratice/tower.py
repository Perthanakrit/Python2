# tower : https://programming.in.th/tasks/1031
'''
2 6 5
1 2
1 3
2 5
3 4
5 6
'''


def use_power(idx: int, power: int):
    max_floor = 0
    curr_floor = stairs[idx][0]
    for i in range(idx, len(stairs)):
        if stairs[i][0] <= curr_floor and curr_floor <= stairs[i][1]:
            if power >= (stairs[i][1] - curr_floor):
                curr_floor = stairs[i][1]
                if max_floor < curr_floor:
                    max_floor = curr_floor
    return max_floor


[power, tower, stair] = [int(x) for x in input().split()]
print(power, tower, stair)

stairs = []

for i in range(stair):
    [y_1, y_2] = [int(x) for x in input().split()]
    stairs.append((y_1, y_2))
print(stairs)

max_floor = 0
for j in range(stair):
    if (stairs[j][0] == 1):
        top_floor = use_power(j, power)
        print(top_floor)
    if (top_floor > max_floor):
        max_floor = top_floor

print(max_floor)
