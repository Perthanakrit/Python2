'''
[[]
 []
 []]
 096000008000300040000240000001000089000803700007590000002451000105006900370980160

{   ['0', '9', '6', '0', '0', '0', '0', '0', '8'], 0
    ['0', '0', '0', '3', '0', '0', '0', '4', '0'], 1
    ['0', '0', '0', '2', '4', '0', '0', '0', '0'], 2
    ['0', '0', '1', '0', '0', '0', '0', '8', '9'], 3
    ['0', '0', '0', '8', '0', '3', '7', '0', '0'], 4
    ['0', '0', '7', '5', '9', '0', '0', '0', '0'], 5
    ['0', '0', '2', '4', '5', '1', '0', '0', '0'], 6
    ['1', '0', '5', '0', '0', '6', '9', '0', '0'], 7
    ['3', '7', '0', '9', '8', '0', '1', '6', '0'] } 8
'''


def CreateGrid(stringToCrateTable):
    row = []
    while True:
        for y in stringToCrateTable:
            if (len(row) <= COL_SIZE):
                if (y != ' '):
                    row.append(y)
                if (len(row) == COL_SIZE):
                    gridList.append(row)
                    row = []

        if (len(gridList) >= ROW_SIZE):
            break


def CheckingToFillBlank(row, column, num):
    for x in range(ROW_SIZE):
        if (gridList[row][x] == num):
            return False
    for y in range(COL_SIZE):
        if (gridList[y][column] == num):
            return False

    start_r = (row // 3) * 3  # (2,5) -> (0,3)(0,4) (5,2)-> (3,0)
    start_c = (column // 3) * 3

    for r in range(3):
        for c in range(3):
            if (gridList[start_r + r][start_c + c] == num):
                return False

    return True


def FillGrid():
    for r in range(ROW_SIZE):
        for c in range(COL_SIZE):
            if (gridList[r][c] == "_"):
                for num in NUM_LIST:
                    if (CheckingToFillBlank(r, c, num) == True):
                        gridList[r][c] = num

                        if (FillGrid()):
                            return True

                        gridList[r][c] = "_"
                return False

    return True


def DisplayGrid():
    index = 0

    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            index += 1
            if (gridList[row][col] == "0"):
                gridList[row][col] = "_"

        print("  {0}  {1}  {2}   {3}  {4}  {5}   {6}  {7}  {8}".format(
            gridList[row][0], gridList[row][1], gridList[row][2], gridList[row][3],
            gridList[row][4], gridList[row][5], gridList[row][6], gridList[row][7], gridList[row][8]))

        if (index % 27 == 0):
            print()


gridList = []
ROW_SIZE = 9
COL_SIZE = 9
NUM_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

if __name__ == "__main__":
    grid = input("Please input grid : ")
    print()
    CreateGrid(grid)
    DisplayGrid()
    print('-------------------------------')
    print()
    if (FillGrid() == True):
        DisplayGrid()
    
    # print(gridList)
    # CreateGrid(grid)
