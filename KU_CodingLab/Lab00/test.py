countX = 0
'''
    [[' x',   x  x  x   x
      ' 1',  28  x  x   69
      ' 2',  26  x  56  x
      ' 6',   x  x  x   75
      ' 3'], 20  x  57  x
               
'''
exampleList = [[' x', ' 1', ' 2', ' 6', ' 3'],
               [' x', '28', '26', ' x', '20'],
               [' x', ' x', ' x', ' x', ' x'],
               [' x', ' x', '56', ' x', '57'],
               [' x', '69', ' x', '75', ' x']]

xChar = " x"

for i in range(4):
    stopLoop = False
    print(f"Round: {i}")

    for j1 in range(3):
        countX = 0
        maxConunt = 0
        maxConunt = 4 - j1
        for n in range(maxConunt):
            match i:
                case 0:
                    '''
                        - (0,1) (1,2) (2,3) (3,4)
                        - (0,2) (1,3) (2,4)
                    '''
                    if (exampleList[n][j1 + 1 + n] == xChar):
                        print(
                            "{2} -- col: {0}, row: {1}, max = {3}".format(n, j1 + 1 + n, j1, maxConunt))

                case 1:
                    if (exampleList[j1 + 1 + n][4 - n] == xChar):
                        print(
                            "{2} -- col: {0}, row: {1}, max = {3}".format(j1 + 1 + n, 4 - n, j1, maxConunt))
                        countX += 1
                case 2:
                    '''
                        (4,3) (3,2) (2,1) (1,0)
                        (4,2) (3,1) (2,0)
                    '''
                    if (exampleList[4 - n][maxConunt - 1 - n] == xChar):
                        print("{2} -- col: {0}, row: {1}, max = {3}".format(4 -
                                                                            n, maxConunt-1 - n, j1, maxConunt))
                        countX += 1
                case 3:
                    '''
                    (3,0) (2,1) (1,2) (0,3) 
                    (2,0) (1,1) (0,2)
                    '''
                    if (exampleList[3 - j1 - n][n] == xChar):
                        print(
                            "{2} -- col: {0}, row: {1}, max = {3}".format(3 - j1 - n, n, j1, maxConunt))
                        countX += 1

        if (countX == maxConunt):
            print(countX)
            stopLoop = True

    for j2 in range(5):
        countX2 = 0
        if (i == 0):
            if (exampleList[j2][j2] == xChar):
                print(j2, j2)
                countX2 += 1
        elif (i == 1):
            if (exampleList[j2][4 - j2] == xChar):
                countX2 += 1
        if (countX2 == 5):
            print("countX2: {0}".format(countX2))
            stopLoop = True

    if (stopLoop):
        break
