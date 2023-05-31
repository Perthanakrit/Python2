def CreateTable(width, height):
    num = 0
    for y in range(height):
        numLst = []    
        for i in range(width):
            num += 1
            numLst.append(num)
            #print ((num), end=' ') if num > 9 else print ("{0}{1}".format(" ", num ), end=' ')

        tableDic[y+1] =  numLst 
        #print ()

def DisplayTable():
    for k in tableDic.keys():
        for j in tableDic[k]: # tableDic[key] = value
            print (j, end=' ') if j > 9 else print ("{0}{1}".format(" ", j ), end=' ')

        print ()

tableDic = {}

if __name__ == '__main__':
    CreateTable(9, 9)
    DisplayTable()
    
