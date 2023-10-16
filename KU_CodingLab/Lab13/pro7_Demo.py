def round_bomb():
    return ""


size_table = input().split("x")
nRow, nCol = int(size_table[0]), int(size_table[1])

nBombs = int(input())
bombs_loca_ls = []
for _ in range(nBombs):
    loca_ls = input().split(",")
    bombs_loca_ls.append( (int(loca_ls[0]), int(loca_ls[1])) ) 
#print(bombs_loca_ls)
board = []
for _ in range(nRow):
    board.append( [0] * nCol)
#print(board)

for loc in bombs_loca_ls:
    y, x = loc[0], loc[1]
    board[y][x] = "*"
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            target_x = x+dx
            target_y = y+dy            
            if 0 <= target_x < nCol and 0 <= target_y < nRow:
                if board[target_y][target_x] != "*":
                    board[target_y][target_x] += 1  
for row in  board:
    for col in row:
        print(col, end="")
    print("")

'''
y, x = loc[0], loc[1] # x = col,  y = row
    board[y][x] = "*"
    # +1 to al adiacent locations
    target_x = x - 1
    target_y = y - 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1 
        
    target_x = x - 1
    target_y = y
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1  
            
    target_x = x - 1
    target_y = y + 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1  
    
    target_x = x + 1
    target_y = y + 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1  

    target_x = x + 1
    target_y = y - 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1     
    
    
    target_x = x + 2
    target_y = y + 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1      


    target_x = x + 2
    target_y = y
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1  
            
    target_x = x + 2
    target_y = y - 1
    if 0 <= target_x < nCol and 0 <= target_y < nRow:
        if board[target_y][target_x] != "*":
            board[target_y][target_x] += 1 
'''