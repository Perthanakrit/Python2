def factorail_result(num:int):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


n = int(input("Enter n: "))
print(f"{n}!", "=", factorail_result(n))