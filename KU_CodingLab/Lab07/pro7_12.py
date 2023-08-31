num_of_times = 1
sum_of_n1n2 = 0
player_result = 0
target = 0

while True:
    n1 = int(input())
    n2 = int(input())
    if n1 > 6 or n1 <= 0  or n2 <= 0 or n2 > 6:
        print("ERROR")
        continue
    sum_of_n1n2 = n1 + n2
    
    if (num_of_times == 1):
        if (sum_of_n1n2 == 7 or sum_of_n1n2 == 11):
            player_result = "W"
            break
        elif (sum_of_n1n2 == 2 or sum_of_n1n2 ==3 or sum_of_n1n2 == 12):
            player_result = "L"
            break 
        else:
            target = sum_of_n1n2
    else:
        if (sum_of_n1n2 == 7):
            player_result = "L"
            break        
        if (target == sum_of_n1n2):
            player_result = "W"
            break
            
            
        
    num_of_times += 1

print(f"{num_of_times} {sum_of_n1n2} {player_result}")