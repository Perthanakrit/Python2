print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

'''
a/b + c/d = (a * d + b * c) / b*d
'''

p = a * d + c * b
q = b * d

print("Summation of the two fractions is {:d} / {:d}".format(p, q))
