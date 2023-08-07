'''
x1 = 0 x2 = 3 -> 3-1 = +2 : east
2 -2 -> -2 - 2 = -4 : west 

y1, y2, y2 - y1
-1  2 -> 2 - (-1) = 3 : north


'''
x_a, y_a = 0, 0
x_b, y_b = 0, 0

distance = 0
horizontal = 0
vertical = 0

direction = ""

while True:
    print("<<Point a>>")
    x_a = int(input("Enter x coordinate: "))
    y_a = int(input("Enter y coordinate: "))

    print("<<Point b>>")
    x_b = int(input("Enter x coordinate: "))
    y_b = int(input("Enter y coordinate: "))

    if (x_a == 0 and y_a == 0) and (x_b == 0 and y_b == 0):
        print("Goodbye")
        break

    direction_x = ""
    direction_y = ""

    print(f"Distance between ({x_a}, {y_a}) and ({x_b}, {y_b}):")

    distance = ((x_a - x_b)**2 + (y_a - y_b)**2)**0.5
    print(f"Euclidean distance is {distance:.2f}.")

    horizontal = abs(x_a - x_b)
    print(f"Horizontal distance is {horizontal}.")

    vertical = abs(y_a - y_b)
    print(f"Vertical distance is {vertical}.")

    if (x_a == x_b and y_a == y_b):
        print("We are going nowhere.")
        continue

    # y direction
    if (y_b - y_a > 0):
        direction_y = "north"
        direction = direction_y
    elif (y_b - y_a < 0):
        direction_y = "south"
        direction = direction_y

    # x direction
    if (x_b - x_a > 0):
        direction_x = "east"
        direction = direction_x
    elif (x_b - x_a < 0):
        direction_x = "west"
        direction = direction_x

    if (direction_y and direction_x):
        direction = f"{direction_y}-{direction_x}"

    print(f"We are going {direction}.")
