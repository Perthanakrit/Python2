'''
15
3
92
6
9
30
41
18
25
35
80
45
60
14
67
75
'''


def similar_value(ls: list):
    minn_similar = float("inf")
    # num_pair_ls = []
    for i in range(len(ls) - 1):
        # print(ls[i+1] - ls[i] < minn_similar)
        if ls[i+1] - ls[i] <= minn_similar:
            minn_similar = ls[i+1] - ls[i]
            # print(ls[i], ls[i+1])
            # num_pair_ls.append((ls[i], ls[i+1]))
    return minn_similar


n = int(input())
hp_lst = sorted([int(input()) for i in range(n)])
# hp_lst = sorted(hp_lst)
value = similar_value(hp_lst)
for i in range(n - 1):
    if hp_lst[i+1] - hp_lst[i] == value:
        print(hp_lst[i], hp_lst[i+1])
