def correct_position():
    correct = 0
    pos = 0
    for i in range(len(copy_target)):
        if guess[pos] == target[pos]:
            correct += 1
            target.pop(pos)
            guess.pop(pos)
        else:
            pos += 1
    return correct

def wrong_position():
    wrong = 0
    for g in guess:
        if g in target:
            wrong += 1
            target.remove(g)
    return wrong

target = list(input())
copy_target = [ch for ch in target]
guess = list(input())

correct_score = correct_position()
wrong_score = wrong_position()

print(f"{correct_score}-{wrong_score}")

'''
pant
test
'''