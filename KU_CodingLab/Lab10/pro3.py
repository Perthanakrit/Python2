def find_sd(score_lst):
    av_score = sum(score_lst) / len(score_lst) 
    print(f"Average score is {av_score:.2f}.")
    summ_score = 0
    for score in score_lst:
        summ_score += ((score - av_score) ** 2)

    return (summ_score / (len(score_lst) - 1)) ** (1/2)

scores = []

while True:
    input_num = float(input("Enter score: ")) 
    if (input_num == -1):
                
        break
    if (input_num > 100 or input_num < 0):
        print("Score is out of range.")
        continue
    scores.append(input_num)

if (len(scores) > 0):
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Standard deviation is {find_sd(scores):.2f}.")