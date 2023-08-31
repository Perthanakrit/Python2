import math

def sqrt_n_times(x, n):
     count = 0
     result = 0
     while  count < n:
          x = math.sqrt(x)
          count += 1
     return x    
          
x = float(input())
n = int(input())
    
print( sqrt_n_times(10**8, 3) )
