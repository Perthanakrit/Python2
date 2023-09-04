def fibonacci(n:int):
    a1 = 0
    a2 = 1
    result = 0
    i = 0
    while i < n:
        result = a1 + a2
        a2 = a1
        a1 = result   
        i += 1
    return result


n = int(input("Enter n: "))

print("fibo({0}) = {1}".format(n,fibonacci(n)))


'''

0 1 
1 1
1 1 2
'''