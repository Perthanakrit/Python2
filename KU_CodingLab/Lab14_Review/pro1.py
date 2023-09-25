def remove_duplicates(lst):
    new_lst = [lst[0]]
    for el in lst:
        count = 0
        for new_el in new_lst:
            if (new_el != el):
                count += 1
            if (count >= len(new_lst)):
                new_lst.append(el)
    return new_lst
    
def sorting(lst):
    lst.sort()
    result_lst = remove_duplicates(lst)
    return result_lst

word = input().lower()

if(word.isalpha()):
    bigrams = []
    if (len(word) < 1):
        word = 'a'
        
    for i in range(len(word) - 1):
        txt = word[i] + word[i+1]
        bigrams.append(txt)
      
    for bigram in sorting(bigrams):
        print(bigram)
        
#print(bigrams[0][0])