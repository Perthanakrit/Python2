def count_elements(formula):
    element_counts = {}  # Dict
    current_element = ''
    count = 0

    for char in formula:
        if char.isupper():
            # Start of a new element
            if current_element:
                element_counts[current_element] = element_counts.get(
                    current_element, 0) + count
            current_element = char
            count = 1
        elif char.islower():
            # Lowercase letter, part of the current element symbol
            current_element += char
        elif char.isdigit():
            # Numeric digit, part of the count
            count = count * 10 + int(char)
        else:
            # Non-alphanumeric character, end of the current element
            if current_element:
                element_counts[current_element] = element_counts.get(
                    current_element, 0) + (count or 1)
            current_element = ''
            count = 0

    # Handle the last element in the formula
    if current_element:
        element_counts[current_element] = element_counts.get(
            current_element, 0) + (count or 1)

    return element_counts

# 3Mg(NO3)2


def my_count_elements(formula):
    elementsDict = {}
    current_element = ""
    count = 0
    time_el = 1

    value = 1
    element_in_bracket = []
    if ("(" in formula):
        open_bracket = formula.index("(")
        close_bracket = formula.index(")")

        for i in range(open_bracket+1, close_bracket+1):
            if (formula[i] != "(" and formula[i] != ")" and formula[i].isalpha()):
                element_in_bracket.append(formula[i])
            if (formula[i+1].isdigit() and formula[i] == ")"):
                value *= int(formula[i+1])
            # elif (formula[i].isdigit()):
            #     value = int(formula[i])

        # print(element_in_bracket)
        # print(value)

    for c in range(len(formula)):
        char = formula[c]
        if char.isupper():
            count = 1
            current_element = char

            if (elementsDict.get(char) is not None):
                print(char)
            if (formula[c+1].islower()):
                continue

            elementsDict[current_element] = 1

            if (elementsDict[current_element] >= 1):
                numOf = elementsDict[current_element] * time_el

                if (char in element_in_bracket):
                    numOf *= value
                    # print("1", char, numOf)

                elementsDict.update({current_element: numOf})
        elif char.islower():
            previous_char = current_element
            current_element += char
            elementsDict[current_element] = elementsDict.pop(previous_char)
        elif char.isdigit():
            # print(current_element)
            if (c == 0):
                time_el = int(char)
            elif (c != 0 and formula[c-1] == current_element):
                elementsDict[current_element] *= int(char)
                # print("2", current_element, [current_element], int(char))
                count = 0

    print("time_el =", time_el)

    return elementsDict


def my_count_element_2(formula):
    elementsDict = {}
    current_element = ""
    times_el = 1

    value = 1
    element_in_bracket = []

    if ("(" in formula):
        open_bracket = formula.index("(")
        close_bracket = formula.index(")")

        for i in range(open_bracket+1, close_bracket+1):
            if (formula[i] != "(" and formula[i] != ")" and formula[i].isalpha()):
                element_in_bracket.append(formula[i])
            if (formula[i+1].isdigit() and formula[i] == ")"):
                value *= int(formula[i+1])

    for c in range(len(formula)):
        char = formula[c]
        if char.isupper() and formula[c + 1].islower() == False:
            if (elementsDict.get(char) is not None):
                elementsDict[char] += 1 * times_el
            else:
                current_element = char
                elementsDict[current_element] = 1 * times_el

            if (current_element in element_in_bracket):
                elementsDict[current_element] *= value

        elif char.islower() and formula[c - 1].isupper():
            current_element = formula[c - 1] + char
            elementsDict[current_element] = 1 * times_el
            if (current_element in element_in_bracket):
                elementsDict[current_element] *= value
        elif char.isdigit():
            # print(current_element)
            if (c == 0):
                times_el = int(char)
            elif (c != 0 and formula[c-1] in current_element):
                elementsDict[current_element] *= int(char)
                # print("2", current_element, [current_element], int(char))
                # count = 0

    return elementsDict


def edit_form(formula):
    # formula[formula.index("(")] = "["
    charRemeOpBarket = 0
    char_Reme_Cl_barket = 0

    for char in formula.split():
        if (char == "(" and charRemeOpBarket == 0):
            char = "["
            charRemeOpBarket += 1
        elif (char == ")" and char_Reme_Cl_barket > 0):
            char = "]"
            char_Reme_Cl_barket = 0

    return formula


# Test the function
formula = input("Enter molecule formula: ")
if (formula[len(formula)-1].isdigit() == False):
    formula += "1"


print(formula)
elements = my_count_element_2(formula)
print("Element counts:", elements)

# Na2(B4O5(OH)4)
# txt = "3Mg(NO3)2"  # "H2O"
# count = 0
# value = 0
# if ("(" in txt):
#     open_bracket = txt.index("(")
#     close_bracket = txt.index(")")

#     for i in range(open_bracket+1, close_bracket+1):
#         if (txt[i+1].isdigit() and txt[i] == ")"):
#             print(txt[i+1])
#             value *= int(txt[i+1])
#         elif (txt[i].isdigit()):
#             value = int(txt[i])

# print(value)
# print(txt.index("3"))
