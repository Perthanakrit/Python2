# function : len(), range()
# methon X.append()

'''def factors(number):
    factors = []
    for factor in range(1, number+1):
        if number % factor == 0:
            factors.append(factor)
    return factors

#print('Factors of 27 is:', factors(27))
'''

#data = []

#while True:
    #txt = input()
    #if (txt == ''):
        #break
    #data.append(txt)

#print(data)
'''
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( max(days) )

scores = [60, 70, 85, 66, 70, 0, 15, 9]
min_score = min(scores)
print(min_score)

scores = [60, 70, 85, 66, 70, 0, 15, 9]
min_score = min(scores)
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( min(days) ) # หา min จากลำดับ a-z (ascii)

len("hello world\n\t" นับ escape char

'''
import math

data = []
max_len_str = -math.inf
max_str = ''

i = 0
while True:
    x = input()
    if (x == ''):
        print(max_str)
        break
    data.append(x)
    if (len(data[i]) > max_len_str):
        max_len_str = len(data[i])
        max_str = data[i]
    i += 1
            