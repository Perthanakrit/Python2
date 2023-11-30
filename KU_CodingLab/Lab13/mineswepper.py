'''
8x10
4
1,1
2,4
5,2
6,8
'''


[size_col, size_row] = [int(x) for x in input().split("x")]
numof_bomb = int(input())

# create board
board = [[0] * size_row for i in range(size_col)]
# set bomd
for i in range(numof_bomb):
    [col, row] = [int(v) for v in input().split(",")]
    board[col][row] = "*"
    '''
    0,0 0,1 0,2
    1,0 1,1 1,2
    '''
    for c in [-1, 0, 1]:
        for r in [-1, 0, 1]:
            target_c = col + c
            target_r = row + r
            if 0 <= target_c < size_col and 0 <= target_r < size_row:
                if board[target_c][target_r] != "*":
                    board[target_c][target_r] += 1

# display
for c in board:
    for r in c:
        print(r, end="")
    print()
