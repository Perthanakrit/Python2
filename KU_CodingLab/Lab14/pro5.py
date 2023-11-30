def sort_auctioneers(auctioneer_dict: dict):
    ls = [auc for auc in auctioneer_dict]
    ls = sorted(ls)
    new_dict = {}

    for item in ls:
        new_dict[item] = auctioneer_dict[item]

    return new_dict


def find_the_winner(m_dict: dict):
    winner = ""
    prev = float("-inf")
    for a in m_dict:
        if m_dict[a][0] > prev and m_dict[a][0] > 0:
            prev = m_dict[a][0]
            winner = a

    return winner


auctioneers = {}
order = 1
winner = ""
while True:
    txt = input()
    if "end" == txt or "" == txt:
        winner = find_the_winner(auctioneers)

        break
    auction_ls = txt.split()
    if len(auction_ls) != 2:
        continue

    input_auctioneer, priece = auction_ls
    priece = float(priece)
    if priece < 0:
        continue
    if input_auctioneer not in auctioneers:
        auctioneers[input_auctioneer] = [priece, 1]
    else:
        times = auctioneers[input_auctioneer][1] + 1
        if (auctioneers[input_auctioneer][0] > priece):
            priece = auctioneers[input_auctioneer][0]
        auctioneers[input_auctioneer] = [priece, times]

if len(auctioneers) > 0:
    auctioneers = sort_auctioneers(auctioneers)
    # rint(auctioneers)

    for auctioneer in auctioneers:
        times = "times" if auctioneers[auctioneer][1] > 1 else "time"
        print(
            f"{auctioneer} bid at the price of {auctioneers[auctioneer][0]:.1f} baht in {auctioneers[auctioneer][1]} {times}.")

    if winner != "":
        print(f"The winner is {winner}.")
'''
ข้อมูลเข้า	ข้อมูลออก
kong 100
saac 1000
kong 300
pp 1000
saac 900
end
'''
