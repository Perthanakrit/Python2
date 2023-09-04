import math
import matplotlib.pyplot as plt

n = int(input())
count = 0

used_n = n - 1 if (n % 2 == 0) else n

num_dash = 0
symbol_dash = used_n // 2

while count < n:
    symbol_star = 0 if (count == 0 or count == n-1) else 1

    if count < math.ceil(n/2):
        num_dash = num_dash if (n // 2 == count and n %
                                2 == 0) else 2 * count - 1
        if (num_dash < 0):
            num_dash = 0
        text = "-" * symbol_dash + "*" * \
            (symbol_star) + "-" * (num_dash) + "*"+"-" * symbol_dash
        symbol_dash -= 1
    else:
        symbol_dash += 1
        text = "-" * symbol_dash + "*" * \
            (symbol_star) + "-" * (num_dash) + "*"+"-" * symbol_dash
        num_dash = 0 if (num_dash // 2 <= 0) else count//2

    print(text)
    count += 1


a = 3

is_prime = True
if (a < 2):
    is_prime = False
elif (a == 2):
    is_prime = True
elif (a % 2 == 0):
    is_prime = False
elif (a > 2):
    for i in range(3, a, 2):
        if (a % i == 0):
            is_prime = False
            break
print(is_prime)
