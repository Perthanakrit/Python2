# len = length
# range 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

i = 0
while i < len(primes):
    primes[i] = primes[i] * 2
    i += 1
print(primes)