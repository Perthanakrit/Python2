'''
pyramid ffgg
program gggf
1-3 (correct position - wrong position)

ab cd
vb bc
pant
test
'''

def find_positions(target, guess):
    correct_position = 0
    wrong_position = 0

    ch_in_guess = []

    for i in range(len(target)):
        if guess[i] == target[i]:
            correct_position += 1
            ch_in_guess.append(guess[i])
            
    if (target != guess):
        for i in range(len(target)):
            if guess[i] in target and guess[i] not in ch_in_guess:
                wrong_position += 1
                ch_in_guess.append(guess[i])
        
    print(ch_in_guess)
    return correct_position, wrong_position

target = [ch for ch in input()]
guess = [ch for ch in input()]
#print(target, guess)

correct_position, wrong_position = find_positions(target, guess)

print(f"{correct_position}-{wrong_position}")
