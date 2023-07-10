'''
    14 27 x 48 74     
    1 28  x  x 69   
    2 26  x 56  x   
    6  x  x  x 75   
    3 20  x 57  x

[x][x] 

'''

import random

tableList = []

definedTableList = [['14', ' 6', ' 5', ' 1', '11'],
                    ['29', '18', '20', '25', '22'],
                    ['31', '42', ' x', '41', '43'],
                    ['47', '58', '49', '48', '57'],
                    ['62', '71', '70', '67', '74']]

COL_SIZE = 5
ROW_SIZE = 5

state = str("Preparation")
randomedNumLst = []

SCORE_FOR_BINGGO = 4
binggoType = ["colum", "row", "diagonal", "square"]


def CreateTable():
    print('-----------------------')
    #random.seed(seed)
    for r in range(COL_SIZE):
        row = []
        for c in range(ROW_SIZE):
            num = GenerateNumber(1 + 15*r, 15*(r+1))
            checkcount = int(0)
            '''if (len(row) > 0):
                for i in range(len(row)):
                    if (row[i] != num):
                        checkcount += 1

                if (checkcount == len(row)):
                    numOfLst += 1
                    row.append(num)
                    checkcount = 0  '''

            row.append(str(num) if num > 9 else ' '+str(num))
            # numOfLst += 1

        tableList.append(row)

    return tableList


def DisplayTable(table):
    global state
    global randomedNumLst
    table[2][2] = " x"
    count = int(1)
    binggoScore = 0

    for el in range(len(definedTableList)):
        '''if (definedTableList[el] != tableList[el]):
            tableList[el] = definedTableList[el]'''

    while True:
        match state:
            case "Preparation":
                print("Here is your table!")
                PrintForm()
                for r in range(ROW_SIZE):
                    print(" " * 4, end='')
                    for c in range(COL_SIZE):
                        print(table[c][r], end=' ')
                    print()

                print()
                print('-----------------------')

                state = "Playing"
                randomedNumLst = []
                random.seed(seed)
            case "Playing":
                num = int(0)
                # play Bingo
                num = GenerateNumber(1, 75)
                table = Play(num, table)
                count += 1

                binggoScore += CheckingBinggo()

                if (len(binggoType) == 0):  # binggoScore >= SCORE_FOR_BINGGO):
                    print("Win at turn: {0}".format(str(count)))
                    PrintForm()
                    for r in range(ROW_SIZE):
                        print(" " * 4, end='')
                        for c in range(COL_SIZE):
                            print(table[c][r], end=' ')
                        print()

                    print()
                    break


def Play(num, table):
    for r in range(ROW_SIZE):
        for c in range(COL_SIZE):
            if (table[c][r] == str(num)):
                tableList[c][r] = " x"

    return table


def RandomNumberGenerator(start, stop):
    return random.randint(start, stop)


def GenerateNumber(start, stop):
    num = 0
    notCopyCount = 1
    if len(randomedNumLst) > 0:
        running = True
        while running:
            num = RandomNumberGenerator(start, stop)
            if (num in randomedNumLst):
                continue
            else:
                randomedNumLst.append(num)
                running = False
                return num
    else:
        num = RandomNumberGenerator(start, stop)
        randomedNumLst.append(num)
        return num


def PrintForm():
    print()
    print(4*" " + "B  I  N  G  O")
    print(4*" " + "--------------")


def CheckingBinggo():
    includeScore = 0
    if ("colum" in binggoType):
        for c in range(COL_SIZE):
            includeScore += BinggoOnColum(c)

    if ("row" in binggoType):
        for c in range(COL_SIZE):
            includeScore += BinggoOnRow(c)

    if ("square" in binggoType):
        for c in range(COL_SIZE - 1):
            includeScore += BinggoOnSquare(c)

    if ("diagonal" in binggoType):
        includeScore += BinggoOnDiagonal()

    if (includeScore >= 1):
        return includeScore
    else:
        return 0


def BinggoOnRow(colum):
    for row in range(ROW_SIZE):
        if (tableList[colum][row] == " x"):
            if colum != 0 and colum != len(tableList) - 1:
                if (tableList[colum - 1][row] == " x" and tableList[colum + 1][row] == " x"):
                    binggoType.remove("row")
                    return 1

    return 0


def BinggoOnColum(colum):
    countX = 0
    for row in range(ROW_SIZE):
        if (tableList[colum][row] == " x"):
            countX += 1

        if (countX == ROW_SIZE):
            binggoType.remove("colum")
            return 1

    return 0


def BinggoOnDiagonal():
    xChar = " x"
    stopChecking = False
    for i in range(4):
        for j1 in range(3):
            maxConunt = 0
            countX = 0

            maxConunt = 4 - j1
            for n in range(maxConunt):
                match i:
                    case 0:
                        if (tableList[n][j1 + 1 + n] == xChar):
                            # print("{2} -- col: {0}, row: {1}, max = {3}".format(n, j1 + 1 + n, j1, maxConunt))
                            countX += 1

                    case 1:
                        if (tableList[j1 + 1 + n][4 - n] == xChar):
                            # print("{2} -- col: {0}, row: {1}, max = {3}".format(j1 + 1 + n, 4 - n, j1, maxConunt))
                            countX += 1
                    case 2:
                        '''
                            (4,3) (3,2) (2,1) (1,0)
                            (4,2) (3,1) (2,0)
                        '''
                        if (tableList[4 - n][maxConunt - 1 - n] == xChar):
                            # print("{2} -- col: {0}, row: {1}, max = {3}".format(4 - n, maxConunt-1 - n, j1, maxConunt))
                            countX += 1
                    case 3:
                        '''
                        (3,0) (2,1) (1,2) (0,3) 
                        (2,0) (1,1) (0,2)
                        '''
                        if (tableList[3 - j1 - n][n] == xChar):
                            # print("{2} -- col: {0}, row: {1}, max = {3}".format(3 - j1 - n, n , j1, maxConunt))
                            countX += 1

            if (countX == maxConunt):
                # print(countX)
                stopChecking = True

        for j2 in range(5):
            countX2 = 0
            if (i == 0):
                if (tableList[j2][j2] == xChar):
                    countX2 += 1
            elif (i == 1):
                if (tableList[j2][4 - j2] == xChar):
                    countX2 += 1
            if (countX2 == 5):
                stopChecking = True

        if (stopChecking):
            binggoType.remove("diagonal")
            return 1

    return 0


def DiagonalPath(col, row):
    trueCount = 0
    for i in range(row):
        if (tableList[col + i][i] != " x"):
            break
        else:
            trueCount += 1
            if (trueCount >= 5):
                return True

    return False


def BinggoOnSquare(colum):
    countX = 0
    for r in range(ROW_SIZE - 1):
        match r:
            case 0:
                if (SquareArea(colum, r, 1)):
                    binggoType.remove("square")
                    return 1
            case 1:
                if (SquareArea(colum, r, -1)):
                    binggoType.remove("square")
                    return 1
            case _:
                if (SquareArea2(colum, r)):
                    binggoType.remove("square")
                    return 1

    return 0


def SquareArea(col, row, num):
    return (tableList[col + num][row] == " x" and tableList[col + num][row+1] == " x" and tableList[col][row+1] == " x")


def SquareArea2(col, row, ):
    return (tableList[col + 1][row] == " x" and tableList[col + 1][row+1] == " x" and tableList[col][row+1] == " x") and (
        tableList[col - 1][row] == " x" and tableList[col - 1][row+1] == " x" and tableList[col][row+1] == " x")


seed = int(input("Input seed: "))
random.seed(seed)

preparTable = CreateTable()
DisplayTable(preparTable)

