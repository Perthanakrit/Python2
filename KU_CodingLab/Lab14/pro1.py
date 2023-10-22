def count_char(word: str):
    char_dict = {}
    for char in word:
        if char.isalpha():
            char = char.lower()
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    return char_dict


print(count_char('4, 12, "" Hello, There'))
