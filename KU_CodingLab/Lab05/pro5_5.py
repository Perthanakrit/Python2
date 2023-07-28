height = int(input("Enter height: "))
count = 0
space = height - 1
numm = 0

while (count < height):
    space_btw = (numm * 3 + 4 * (count - 1))
    print(" "*2*space + "1" + " " * (space_btw) + "1" * numm)
    count += 1
    numm = 1

    space -= 1


'''
   1
  1  1
 1    1
'''
'''
        1
      10001
    100000001
  1000000000001
10000000000000001

'''
