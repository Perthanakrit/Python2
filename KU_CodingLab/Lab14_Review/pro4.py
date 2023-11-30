original_text = input().strip()
key = input()
encode_text = input()

key_dict = {}
new_text = ""
key_idx = 0
for i in range(len(original_text)):
    if original_text[i] != " " and original_text[i] not in new_text:
        key_dict[key[key_idx]] = original_text[i]
        new_text += original_text[i]
        key_idx += 1
# print(key_dict)

# decode
decoded_text = ""
for ch in encode_text:
    if ch in key_dict:
        decoded_text += key_dict[ch]
        continue
    decoded_text += ch
print(decoded_text)
