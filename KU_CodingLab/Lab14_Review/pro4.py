original_text = input()
key = input()
encode_text = input()

key_dict = {}
new_text = ""
for i in range(len(original_text)):
    if original_text[i] != " " and original_text[i] not in new_text:
        key_dict[key[i]] = original_text[i]
        new_text += original_text[i]
print(key_dict)