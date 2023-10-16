def check_order(l):
    non_increasing_count = 0
    non_decreasing_count = 0
    for i in range(1, len(l)):
        if (l[i] < l[i-1]):
            non_increasing_count += 1
        elif (l[i] > l[i-1]):
            non_decreasing_count += 1
        elif (l[i] == l[i-1]):
            non_decreasing_count += 1
            non_increasing_count += 1

    if (non_increasing_count == non_decreasing_count):
        return "="
    else:
        if (non_increasing_count == len(l) - 1):
            return "-"
        if (non_decreasing_count == len(l) - 1):
            return "+"

    return ""


def display(og_lst: list):
    if og_lst == []:
        print("The list is empty.")
        return
    print("-----")
    print("Original list:")
    print(og_lst)
    case_type = check_order(og_lst)
    if case_type != "":
        if case_type == "-":
            print("The list is in non-increasing order.")
        elif case_type == "+":
            print("The list is in non-decreasing order.")
        elif case_type == "=":
            print("The list is in non-increasing and non-decreasing order.")
    else:
        print("The list is in random order.")


ls = []
while True:
    num = int(input("Enter a number (-1 to end): "))
    if (num == -1):
        display(ls)
        break

    if (0 <= num <= 100):
        ls.append(num)
    else:
        print("Number is out of range.")
