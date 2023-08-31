print("Upper left corner coordinate:")
x_axis_coner = int(input("  << x axis: "))            
y_axis_corner = int(input("  << y axis: "))
eastern = int(input("  << Eastern: "))
southernint = int(input("  << Southern: "))

print("Enter a coordinate:")
x_axis = int(input("  << x axis: "))            
y_axis = int(input("  << y axis: "))

total_x = x_axis_coner + eastern
total_y = y_axis_corner + (-southernint)
      
or_not = ""
if (x_axis_coner <= x_axis <= total_x and total_y <= y_axis <= y_axis_corner):
    or_not = " "
else:
    or_not = " not "

print(f">>> ({x_axis:.2f}, {y_axis:.2f}) is{or_not}inside the rectangle.")