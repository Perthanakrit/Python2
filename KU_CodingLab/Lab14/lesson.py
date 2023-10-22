'''
months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}
'''
# 1. Access by Key


def have_region(provinces):
    if region in provinces:
        return True
    return False


def have_provine(region, provinces, province):
    count = 0
    if region not in provinces:
        return True
    if province not in provinces[region]:
        return True

    return False


provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

provinces_2 = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}
'''
while True:
    text = input()
    if text == "":
        break
    province, region = text.split(":")

    if have_provine(region, provinces, province) or region not in provinces:
        print("No")
        continue
    elif province in provinces[region]:
        print("Yes")
'''

'''
for region in provinces_2:
    # print(provinces_2[region])
    for province in provinces_2[region]:
        print(f"{province}:{region}")
'''
'''
countries = {'th': 'Thailand', 'en': "England", "jp": 'Japan', "kr": "Korea"}
countries.pop('th')  # ลบ key 'th' ออก
print(countries)   
'''

# 2. Access by Value
provinces_3 = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

while True:
    text = input()
    if text == "":
        break
    province, region = text.split(":")
    # print(province)
    provinces_3[region] = provinces_3[region] + [province]
print(provinces_3)
