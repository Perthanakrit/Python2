def cal_take_class(numof_stu: int):
    ls = [0]
    for i in range(numof_stu):
        take_class = 0
        chec_ls = input().split()
        for el in chec_ls:
            if el == "1":
                take_class += 1
        ls.append(take_class / len(chec_ls) * 100)
    return ls


def cal_done_assignment(numof_stu: int, total: int):
    ls = [0]
    for i in range(numof_stu):
        result_done = 0
        done_ls = input().split()
        for done in done_ls:
            result_done += int(done)
        ls.append(result_done / total * 100)
    return ls


def have_right(take_class: float, done_exc: float) -> bool:
    if take_class < criteria[0] and done_exc < criteria[1]:
        return False
    return True


assignments = [int(input_num) for input_num in input().split()]
total_assignments = sum(assignments)
criteria = [float(input_crt)
            for input_crt in input().split()]  # [เข้าเรียน, แบบฝึกหัด]
num_of_students = int(input())

take_class_lst = cal_take_class(num_of_students)
# print(take_class_lst)
done_assignments = cal_done_assignment(num_of_students, total_assignments)
# print(done_assignments)
# [{ 'id': }, ...]
students = []
count_no_right = 0
for i in range(1, num_of_students+1):
    students.append({'id': i, 'take_class': take_class_lst[i],
                    'done_exc': done_assignments[i], 'rights': have_right(take_class_lst[i], done_assignments[i])})
    if not students[i-1]['rights']:
        count_no_right += 1

# print(students)
print(count_no_right)
for student in students:
    id = f"{student['id']}" if student['rights'] else f"({student['id']})"

    print(f"{id} {student['take_class']:.2f} {student['done_exc']:.2f}")
# print(students[0]['id'], students[0]['take_class'], students[0]['done_exc'])
