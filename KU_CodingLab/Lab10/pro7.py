# total exerice
# float: 85 ถ้าน้อยกว่านี้ หมดสิทธิ
# num of studnet each subject
# n... n stedentt
import time 

def disable_stu(lst, done):
    count = 0
    for stu in lst:
        if (done > stu):
            count += 1  
    return count


total_ex = int(input())
done_persent = float(input())
d_persent = done_persent / 100
done_persent = (d_persent) * total_ex

num_of_student = int(input())

stu_done_exs = []

for i in range(num_of_student):
    done_ex = int(input())
    stu_done_exs.append(done_ex)

start = time.time()

num_of_disstu = disable_stu(stu_done_exs, done_persent)
print(num_of_disstu)

for s in range(len(stu_done_exs)):
    persent = (stu_done_exs[s] / total_ex) * 100
    if (done_persent > stu_done_exs[s]):
        print(f"({s+1}) {persent:.2f}")
        continue
    print(f"{s+1} {persent:.2f}")
       
end = time.time()

print(end-start)
