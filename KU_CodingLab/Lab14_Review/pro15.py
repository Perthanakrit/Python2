# hello world

txt = input().split()
except_word = ["for", "and", "with", "of"]
for c in range(len(txt)):
    curr_word = txt[c]
    if curr_word not in except_word:
        txt[c] = curr_word.capitalize()

    # print(word, end=" ")
print(" ".join(txt))
