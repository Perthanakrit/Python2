vowels = ["a", "e", "i", "o", "u"]

input_str = input()
new_str = ""
for ch in input_str:
    if (ch.lower() in vowels):
        new_str += ch.upper()
        continue
    
    new_str += ch.lower()
        
print(new_str)