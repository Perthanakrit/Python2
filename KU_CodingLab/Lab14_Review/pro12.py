'''
C1CnC2Cn-1...C(n/2)C(n/2)+1 ถ้า n เป็นเลขคู่ abcdef	
C1CnC2Cn-1...C((n+1)/2)-1 C((n+1)/2)+1 C((n+1)/2) ถ้า n เป็นเลขคี่ 1234567
'''


def knitting_characters(txt: str):
    new_txt = ""
    for i in range(len(txt)//2 + 1):
        if len(txt) % 2 != 0:
            if i == len(txt)//2:
                new_txt += txt[i]
                continue
        else:
            if i == len(txt)//2:
                break
        new_txt += (txt[i] + txt[-i-1])
    return new_txt


txt = input()
print(knitting_characters(txt))
