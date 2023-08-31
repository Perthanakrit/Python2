def digit(num):
    return num % 10
def tens(num):
    num //= 10
    return num % 10
def hundreds(num):
    num //= 100
    return num % 10
def thousands(num):
    num //= 1000
    return num % 10

def sum_digits(num):
    result = 0
    while num > 0:
        result += (num % 10)
        num //= 10
        
    return result

n = int(input("Enter a number (0 to 9999): "))


print(f"Digit place is {digit(n)}.")
print(f"Tens place is {tens(n)}.")
print(f"Hundreds place is {hundreds(n)}.")
print(f"Thousands place is {thousands(n)}.")
print(f"Sum of all digits is {sum_digits(n)}.")