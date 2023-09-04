def factor_count(num:int):
    d = 1
    count = 0
    
    while d <= num:
        if (num % d == 0):
            count += 1
        d += 1

    return count
    
n = int(input("Enter n: "))
c = factor_count(n)
print(c)