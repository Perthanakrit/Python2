'''
    input : string 3Mg(NO3)2

    (num) A2(B4)3  -> A : 2(num), B : 3 x 4 (num)

    num อยู่ หลัง => ), Element
'''

CHEMICAL_ELEMENTS = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Ni", "Co", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
    "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
    "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv",
    "Ts", "Og"
]

moluculeLst = []
numLst = []
moleculeDict = {}


def FindNumberofMolecules(moluculeLst, numLst):
    pass

def ChceckElement(curr, prev):
    if (prev + curr  in CHEMICAL_ELEMENTS):
        print( prev + curr)
        return True

def NumOfElementsInBracket(curr):
    pass

chemicalFormula = input("Input chemical formula: ")

newEl = ''
numOfEl = 1

for i in range(len(chemicalFormula)):
    elStr = chemicalFormula[i]
    if (elStr.isdigit()):
        if (i == 0):
            numOfEl = int(chemicalFormula[0])
            
    if elStr.isupper():
        if (elStr in CHEMICAL_ELEMENTS):
            if (i != len(chemicalFormula) - 1):
                if (ChceckElement(chemicalFormula[i+1],elStr)):
                    newEl += elStr
                else:
                    moluculeLst.append(elStr)
                    moluculeLst.append(numOfEl)
                    
            else:
                moluculeLst.append(elStr)
                moluculeLst.append(numOfEl)
        else:
            newEl += elStr

    elif elStr.islower():
        if chemicalFormula[i-1].isupper:
            if (ChceckElement(elStr, chemicalFormula[i-1])):
                newEl += elStr
                moluculeLst.append(newEl)
                moluculeLst.append(numOfEl)
                newEl = ''


print()

print(chemicalFormula)
print(moluculeLst)
