'''
papapripikap
'''

word = str(input()).lower()
maxx = 'a'
count = 0
new_word = ''
for char in word:
    if char not in new_word:
        new_word += char

for i in new_word:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        if i >= maxx:
            maxx = i
            count += 1
        else:
            break
    else:
        break
print(count)
