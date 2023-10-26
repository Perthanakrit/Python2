def func(a=1, b=1):
    a += a
    b += b
    return a, b


def func_array(a, e, c=[], d=[]):
    c.append(a), d.append(e)
    return c, d


# i, j] = [i for i in range(2)]
'''
print(func())
print(func(i, j))
print(func(1, 2))
print(func(2))
'''
'''
print(func_array(1, 1))
print(func_array(1, 2))
'''

my_dict = {4: "c", 5: "e", 1: "a", 2: "b", 3: "c"}
print(my_dict.get(4, "d"))
print(my_dict.keys())
# print(sorted(list(my_dict.items()))) -> [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'c'), (5, 'e')]
my_dict = dict(sorted(list(my_dict.items())))
# print(my_dict)
print(my_dict.pop(6))
# print(my_dict)
# d2 = {4: "c", 6: "f", 7: "g"}
# my_dict = {**my_dict, **d2} -> {**my_dict, 6: "f", 7: "g"}
# my_dict.update(d2)
# print(my_dict)
