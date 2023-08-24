def display_symbol(line:int, width:int):
    count = 1
    while count <= line:
        w = 1
        while w <= width:
            if (count % 2 == 0):
                print(' *',end='')
            else:
                print('* ',end='')
            
            w += 1
        count += 1
        print()
    

height = int(input("Enter height: "))
width = int(input("Enter width: "))

if (height > 0 and width > 0):
    display_symbol(height, width)
else:
    print("Invalid input, program terminates.")
