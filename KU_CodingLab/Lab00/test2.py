import re

def count_elements(formula):
    num = int(formula[0]) if formula[0].isdigit() else 1
    element_counts = {}
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    print(matches)

    for match in matches:
        element = match[0]
        count = match[1] if match[1] else '1'
        count = int(count)
        element_counts[element] = element_counts.get(element, 0) + num * count #get(key, default_value) -> value

    return element_counts

# Test the function
formula = input("Enter molecule formula: ")
elements = count_elements(formula)
print("Element counts:", elements)







