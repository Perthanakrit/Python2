'''
A 10 8 2 7

 = bot =
   start - A 10
   check card -> 11 -> darw 8 : 1+10+8 > 16
   

'''
def card_to_score(card, c_dict):
    if (card == "A" or card == "K" or card == "Q" or  card == "J"):
        return c_dict[card]
    else:
        return int(card)


def max_card(num, c_dict):
    if (2 <= num <= 10):
        return num
    
    for key in c_dict.keys():
        if (c_dict[key] == num):
            #print(c_dict[key])
            return key

    
top_five_card = input().split(" ")
#print(top_five_card)

cards_dict = {"A":1, "J":11, "Q":12, "K":13 }

cards_hands = []
numof_cards_hand = 0
total_score = 0
for i in range(len(top_five_card)):  
    if (total_score > 16 or numof_cards_hand >= 5):
        break
    numof_cards_hand += 1
    current_card = card_to_score(top_five_card[i], cards_dict)
    cards_hands.append(current_card)
    total_score += current_card if current_card <= 10 else 10
 
max_card = max_card(max(cards_hands), cards_dict)   
#print(cards_hands) 
print(max_card)
print(total_score) if total_score <= 21 else print("busted")