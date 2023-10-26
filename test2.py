def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            print(arr[j + 1], arr[j])
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    print("------")
    return arr


def bubble_sort_v2(arr: list):
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)-1, len(arr) - 1 - i, -1):
            print(arr[j - 1], arr[j])
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


ls = [23, 78, 3, 1, 58, 10, 55]
ls_1 = [10, 20, 25, 3, 30]
# print(bubble_sort_v2(ls_1))
# print(bubble_sort(ls_1))


def insertion_sort_v1(arr: list):
    for i in range(len(arr)):
        hold = arr[i]
        for j in range(i-1, -1, -1):
            print(hold, arr[j], end=", ")
            if arr[j] > hold:
                arr[j], arr[j+1] = hold, arr[j]
        print()
    return arr


# print(insertion_sort_v1([23, 10, 78, 45, 8, 32, 56]))

def binary_search(lst: list, x):
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid  # return when lst[mid] == x
    return "Not Found"


# sorted_ls = bubble_sort([10, 1, 2, 55, 30, 23, 6, 3, 66, 9, 11, 58])
# print(sorted_ls)
target = 0
print(binary_search([1, 2, 3, 6, 9, 10, 11, 23, 30, 55, 58, 66], target))
