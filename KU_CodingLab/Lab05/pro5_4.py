n = int(input())
if (n < 0):
    n *= -1

c = input()
num_of = 1

while (n > 0):
    print(c * num_of)
    num_of += 1
    n -= 1
