#naming convention
# a-zA-z0-9
# snake_case (under_score)
# camelCase
  # lower and UpperCamel
# kebab-case : "-"
# ไม่ซ้ำ keyword
import math

def circle(r):
  return math.pi * (r**2)

def circumference(r):
  return 2 * math.pi * r

def sphere(r):
  return 4/3 * math.pi * (r**3)

r = float(input("Enter a radius: "))

print(f"{circle(r):.2f}")
print(f"{circumference(r):.2f}")
print(f"{sphere(r):.2f}")