def create_lst(txt: str):
    ls = []
    for i in txt:
        if i not in ls:
            ls.append(i)
    return ls


input_txt = input().lower()

if (input_txt != ""):
    word_lst = create_lst(input_txt)
    word_lst.append("")
    for i in range(len(word_lst) - 1):
        if (word_lst[i+1] < word_lst[i] or word_lst[i+1] == ''):
            print(i+1)
            break
else:
    print(0)
