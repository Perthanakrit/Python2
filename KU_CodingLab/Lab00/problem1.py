def CreateTable(width, height):
    num = 0
    for y in range(height):    
        for i in range(width):
            num += 1
            print ("{0}{1}".format() end=' ')
        print ()

if __name__ == '__main__':
    CreateTable(8, 8)