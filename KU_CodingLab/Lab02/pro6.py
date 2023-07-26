import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a1 = math.pow(x, y) + z  # pow : base
print("a1 = %.2f" % (a1))

a2 = math.cos(2*math.pi) + math.log(x)  # log
print("a2 = %.2f" % (a2))

a3 = math.fabs(x) + math.fabs(y)
print("a3 = %.2f" % (a3))

a4 = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
print("a4 = %.2f" % (a4))

a5 = math.pow(math.sin(x), 2) + math.pow(math.cos(x), 2)
print("a5 = %.2f" % (a5))

a6 = math.pow(x+y, 1/5)
print("a6 = %.2f" % (a6))

a7 = math.pow(math.e, x*math.log(y))
print("a7 = %.2f" % (a7))
