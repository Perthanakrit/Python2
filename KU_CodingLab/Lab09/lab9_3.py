def  nb_year(p0, percent, aug, p):
    total_bac = p0
    percent /= 100
    days = 0
    while total_bac < p:
        total_bac = int(total_bac + total_bac * percent + aug)
        
        days += 1
        
    return days

print(nb_year(1500000, 0.25, 1000, 2000000))

'''
p0 + p0 * percent + aug -> comper with p
'''