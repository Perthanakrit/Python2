def simple_interest(p, r, t):
    return p + (p * (r/100) * t)

def compound_interest(p, r, t):
    return p * ((1 + r/100) ** t)

p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print(simple_interest(p, r, t))
print(compound_interest(p, r, t))