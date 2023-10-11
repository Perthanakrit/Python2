def split_name_with_symbols(name):
    # Split the name into words using specified symbols as delimiters
    symbols = "-_=. $"
    words = [name]
    
    for symbol in symbols:
        new_words = []
        for word in words:
            new_words.extend(word.split(symbol))
        words = new_words
    
    return words

def to_camel_case(name):
    # Split the name into words using the specified symbols as delimiters
    words = split_name_with_symbols(name)
    
    # Capitalize the first letter of each word (except the first word)
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    # Join the words together to form the camelCase name
    camel_case_name = ''.join(camel_case_words)
    
    return camel_case_name

# Input the name with symbols
input_name = input("Enter a name with symbols: ")

# Convert to camelCase
camel_case_result = to_camel_case(input_name)

# Print the camelCase result
print("CamelCase Name:", camel_case_result)
