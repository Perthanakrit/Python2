def check_prime(num:int):
    i = 1
    perfect = 0
    if (num < 2 ):
        return False
    else:
        while i <= num:
            if (num % i == 0):
                perfect += 1
            i += 1
    if (perfect <= 2):
        return True

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")