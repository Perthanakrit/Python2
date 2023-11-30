'''
8 5
.....
.....
.OO..
.....
.O...
...O.
.....
....O
1 1 3 2 2
'''

def create_board():
    lst = []
    for i in range(size_col):
        row_ls = [c for c in input()]
        if len(row_ls) == size_row: 
            lst.append(row_ls)
    return lst

def set_brick(idx:int, brick:int):
    stop = False
    for i in range(brick):
        for b in range(len(board) - 1):
            if board[b+1][idx] == "O" or board[b+1][idx] == "#":
                board[b][idx] = "#"
                stop = True
                break
        if not stop:
            board[b+1][idx] = "#" 

[size_col, size_row] = [int(v) for v in input().split()]
board = create_board()
bricks = [int(b) for b in input().split()]

for i in range(len(bricks)):
    set_brick(i, bricks[i])

for col in range(len(board)):
    for row in range(len(board[col])):
        print(board[col][row],end="")
    print()
#print(board)

