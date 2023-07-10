import random

seed = int(input("Input seed: "))

randomedNumLst = []

def RandomNumberGenerator(start, stop):
    return random.randint(start, stop)

def GenerateNumber(start, stop):
    num = 0
    notCopyCount = 1
    if len(randomedNumLst) > 0:
        running = True
        while running:
            
            num = RandomNumberGenerator(start, stop)
            if (num in randomedNumLst):
                continue
            else:
                randomedNumLst.append(num)
                running = False
                return num
    else:
        num = RandomNumberGenerator(start, stop)
        randomedNumLst.append(num)
        return num

for i in range(5):
    random.seed(seed)
    print(GenerateNumber(1, 15))