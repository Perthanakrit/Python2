'''
    nine billion eight hundred and seventy-six million five hundred and forty-three thousand two hundred and nineteen   
    - 9 million + 866 million + 543000 + 209

    two hundred and thirty-nine quadrillion nine hundred and eighty-six trillion five hundred and forty-three billion two hundred and nineteen million eight hundred and sixty-one thousand two hundred and twenty
    wto undecillion 
    ten thousand two hundred and thirty-nine quadrillion nine hundred and eighty-six trillion five hundred and forty-three billion two hundred and nineteen million eight hundred and sixty-one thousand two hundred and twenty
    one billion two hundred thousand three ten thousand one thousand five hundred and fifty-four
    one hundred and ten three
    twelve eleven

    *one three = 4 -> false
    *one hundred one three = 113 -> false 
    '''


def DisplayTotalNumber(numTxtLst):
    totalNum = 0

    for i in numTextLst:
        if (i == ''):
            numTextLst.remove(i)

    for numTxtS in numTxtLst:
        totalNum += ToInt(numTxtS)

    totalNumStr = str(totalNum)[::-1]
    strLst = []
    numStr = str()

    for char in totalNumStr:
        strLst.append(char)

    for i in range(0, len(strLst)):
        index = 1 + i

        if (i % 3 == 0 and i != 0):
            strLst[i] = "," + strLst[i]

        numStr += strLst[i]

    return numStr[::-1]


def ToInt(numTxtS):
    numTxt = numTxtS.split('_')

    numInt = 0
    for num in numTxt:
        if (num != "and"):
            if (num in usaNumShort):
                numInt = 1 if numInt == 0 else numInt
                numInt *= StrToInt(num)
            else:
                numInt += StrToInt(num)

    return numInt


def StrToInt(string):
    return myDict[string]


def InputVerification():
    verifing = True
    while verifing:
        stringVerLst = []
        totalValue = 0
        unavailable = 0
        stringInput = input()

        stringInput = stringInput.translate({45: 95})
        stringVerLst = stringInput.split()
        print(stringVerLst)
        for k in range(len(stringVerLst)):
            if stringVerLst[len(stringVerLst) - 1 - k] != 'and':
                totalValue += StrToInt(stringVerLst[len(stringVerLst) - 1 - k])

            if (k >= 1):
                for v in myDict:
                    if (myDict[v] == totalValue):
                        unavailable += 1

        if (unavailable == 0):
            verifing = False
            return stringInput


myDict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'ten thousand': 10000,
    'hundred thousand': 100000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'decillion': 10000000000000000000000000000000000,
    'undecillion': 10000000000000000000000000000000000000,

}
numTextLst = []
usaNumShort = ['hundred', 'thousand', 'ten thousand', 'hundred thousand', 'million', 'billion', 'quadrillion',
               'trillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion']
valuelst = []

if __name__ == '__main__':
    numText = input()  # InputVerification()

    numText = numText.translate({45: 95})
    removed = False

    textlst = numText.split()

    for txt in range(len(textlst)):

        if (textlst[txt + 1 if txt < len(textlst) - 1 else 0] == 'thousand'):
            if (textlst[txt] == 'ten' or textlst[txt] == 'hundred'):
                textlst[txt] = textlst[txt] + ' thousand'
                removed = True

        # if (removed == False):
        valuelst.append(textlst[txt])

        next = 0
        next = txt+1
        if next > len(textlst) - 1:
            next = len(textlst) - 1

        for i in range(len(usaNumShort)):
            if (usaNumShort[i] == textlst[txt] and textlst[next] != "and"):
                numTextLst.append('_'.join(valuelst))
                valuelst = []
            elif (txt == len(textlst)-1 and usaNumShort[i] != textlst[txt]):
                numTextLst.append('_'.join(valuelst))
                valuelst = []
                break

    # print()
    if (removed):
        for el in numTextLst:
            if (el == 'thousand'):
                numTextLst.remove(el)

    # print(numTextLst)
    print(DisplayTotalNumber(numTextLst))
