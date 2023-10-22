m_dict = {'kong': [300, 2], 'saac': [900, 2], 'pp': [1000, 1]}

prev = float("-inf")
curr = 0
for el in m_dict:
    print(prev, end=" ")
    curr = m_dict[el][0]
    print(curr)
    if curr > prev:
        prev = curr
        winner = el
