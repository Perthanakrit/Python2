total_students = 20
scores = []

i = 1
while i <= total_students:
    score = int(input("Enter score: "))
    if (0 <= score <= 10):
        scores.append(score)
        i += 1
    else:
        print("Score is out of range.")


print("Original list:")
print(scores)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums [0] * 11

for num in nums:
    count = 0
    for score in scores:
        if (num == score):
            count += 1
    txt = '*' * count
    print("{0:>2} {1}".format(num, txt))
