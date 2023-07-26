'''Enter x : 0
f(0.00) = 0'''
import math

x = float(input("Enter x : "))

y = 0

if (x < 0):
    y = math.sqrt(math.pow(x, 2) + 1)
elif (x == 0):
    y = x
elif (x > 0 and x <= 99):
    y = 3 * math.pow(x, 2) - math.pow(1-x, 2)
elif (x > 99):
    y = 2 * math.pow(x, 3) - (x/math.sqrt(x+1))

print(f"f({x:.2f}) = {math.ceil(y)}")
