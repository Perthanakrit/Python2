# len = length
# range

import copy
ls = [5, 15, 6, 7, 1]

# print(ls[4:2:-1])
# print(ls[2::2])
# for i in range(len(ls)):
#     print(ls[i])
# c = ls
ls[-1] = ls[-1] + ls.pop()  # แทน ls[-1] : 1 + 1
print(ls)
# print(c)

ls_2 = [[1, 2], [2, 3]]
ls_copy = ls_2.copy()
# print(ls_copy)
print(ls_2[0] is ls_copy[0])  # True
# ls_2[0].pop()
# print(ls_copy)
'''
import copy
ls_decp = copy.deepcopy(ls_2)
print(ls_decp)
# print(ls_2[0] is ls_decp[0])   # -> False
ls_2[0].pop()
print(ls_decp)
print(ls_2)
'''
