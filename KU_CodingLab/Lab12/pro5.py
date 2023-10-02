def match_word(lst, char, inputs):
    count = 0
    for i in inputs:
        if i == char:
            return count
        
    for el in lst:
        if (el != char):
            lst = lst.replace(el, "-")

    return count

word = input()
input_words = []
match_count = 0
while True:
    get_char = input()
    if (get_char == "0"):
        break  
    
    #match_count += match_word(word,get_char,input_words)  
    input_words.append(get_char)
    
for ch in word:
    if ch not in input_words:
        word = word.replace(ch,"-")

print(word)