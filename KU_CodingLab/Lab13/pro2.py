def validate(lst):
    if len(lst) > 5:
        return True
    for el in lst:
        if el.isalpha():
            if el not in ["A","J","Q","K"]:
                return True
    return False

def card_value(c):
    if c == "A":
        return 1
    if c in ["A","J","Q","K"]:
        return 10

    return int(c)

roundd = int(input())


result_lst = []
for i in range(roundd):
    cards_input = input().split()
    result = 0
    card_on_hand = 0
    
    if validate(cards_input):
        continue
    
    for card in cards_input:
        result += card_value(card)
        card_on_hand += 1 
    
        if result > 16 or card_on_hand >= 5:
            break         
        
    result_lst.append(result)       
        
for res in result_lst: print(res) if res <= 21 else print("busted")

