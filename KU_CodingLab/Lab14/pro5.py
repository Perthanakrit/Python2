def sort_auctioneers(auctioneer_dict:dict):
    ls = [auc for auc in auctioneer_dict]
    ls.sort()
    new_dict = {}
     
    for item in ls:
        new_dict[item] = auctioneer_dict[item]

    return new_dict


def find_the_winner(m_dict: dict):
    winner = ""
    prev = float("-inf")
    for a in m_dict:
        if m_dict[a][0] > prev:
            prev = m_dict[a][0]
            winner = a

    return winner


auctioneers = {}
order = 1
winner = ""
while True:
    auction_ls = input().split()
    if "end" in auction_ls:
        winner = find_the_winner(auctioneers)
        # print(winner)
        break
    if len(auction_ls) != 2:
        continue
    
    input_auctioneer, priece = auction_ls
    priece = float(priece)
    if priece < 0:
        continue
    if input_auctioneer not in auctioneers:
        auctioneers[input_auctioneer] = [priece, 1]
    else:
        if auctioneers[input_auctioneer][0] < priece:
            times = auctioneers[input_auctioneer][1] + 1
            auctioneers[input_auctioneer] = [priece, times]

if len(auctioneers) > 0:
    auctioneers = sort_auctioneers(auctioneers)
    #print(auctioneers)

    for auctioneer in auctioneers:
        times = "times" if auctioneers[auctioneer][1] > 1 else "time"
        print(f"{auctioneer} bid at the price of {auctioneers[auctioneer][0]:.1f} baht in {auctioneers[auctioneer][1]} {times}.")

    print(f"The winner is {winner}.")
'''
per 1000
abc 500
new 1000
abc 1100
per 1500
new 1600
abc 1600
end
'''