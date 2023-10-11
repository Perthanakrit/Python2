'''
[500,2,1000,20,100,1,5]
[500,100,50,10,5,1]
[10,50,5,1,100]
'''

def use_banknote(money:int, card:int):
    num_of = 0
    while money // card > 0:
        num_of = money // card 
        money -= card * num_of
        
    return [num_of,money] 


# input
n = int(input())
banknotes_lst = [int(input()) for i in range(n)]
banknotes_lst.sort(reverse=True)

change = int(input())

for banknote in banknotes_lst:
    ls = use_banknote(change, banknote)
    
    change = ls[1]
    print(f"{banknote}: {ls[0]}")