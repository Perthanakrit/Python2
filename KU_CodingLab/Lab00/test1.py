def ConvertNumberWordsToNumbers(number_words):
    global running

    usaNumShort = ['hundred', 'thousand', 'ten thousand', 'hundred thousand', 'million', 'billion', 'quadrillion',
                   'trillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion']

    words = number_words.split()
    total = 0
    current_value = 0

    print(words)
    for word in words:
        if word == 'and':
            continue
        if word in number_dict:
            if current_value == 0:
                current_value = number_dict[word]
            elif word == 'hundred':
                current_value *= 100
                running = CurrentValueVerfication(current_value)
            elif word in usaNumShort:
                running = CurrentValueVerfication(current_value)
                total += current_value * number_dict[word]

                current_value = 0
            elif current_value > 0:
                current_value += number_dict[word]
                running = CurrentValueVerfication(current_value)

        else:
            if ('-' in word):
                for wN in word.split('-'):
                    current_value += number_dict[wN]

    return total + current_value


def CurrentValueVerfication(current_value):
    print(current_value)
    current_valueInDict = False
    for key in number_dict:
        if current_value == number_dict[key]:
            current_valueInDict = True

    return current_valueInDict


# Test the
number_dict = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
    'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
    'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000,
    'ten thousand': 10000, 'hundred thousand': 100000,
    'million': 1000000, 'billion': 1000000000, 'trillion': 1000000000000,
    'quadrillion': 1000000000000000, 'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000, 'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000, 'nonillion': 1000000000000000000000000000000,
    'decillion': 10000000000000000000000000000000000,
    'undecillion': 10000000000000000000000000000000000000,
}

running = True

while running:
    number_words = input("Enter number words: ")
    number = ConvertNumberWordsToNumbers(number_words)


print("Number:", number)
