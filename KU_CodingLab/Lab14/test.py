def num_of_atoms(idx: int, formal: str):
    i = idx
    num = ""
    if i < len(formal) - 1:
        while formal[i].isdigit():
            num += formal[i]
            # print(num)
            i += 1
    return num if num != "" else "1"


def crate_dict(formal: str):
    my_dict = {}

    for i in range(len(formal)):
        if formal[i].isupper():
            if i+1 < len(formal) and formal[i+1].islower():
                my_dict[formal[i:i+2]] = num_of_atoms(i+2, formal)
            else:
                my_dict[formal[i]] = num_of_atoms(i+1, formal)

    return my_dict


formal_name = input()
if not formal_name[len(formal_name)-1].isdigit():
    formal_name += "1"
target = input()
# print(formal_name)

chem_element_dict = crate_dict(formal_name)
print(chem_element_dict)
if target in chem_element_dict:
    print(chem_element_dict[target])
