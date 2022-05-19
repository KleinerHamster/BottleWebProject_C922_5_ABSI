def conclusionAboutTheWorkElement(A,B,C,D,E
                                  ,numberA,numberB,numberC,numberD,numberE):
    arrayResults=[]

    if(A > numberA):
        arrayResults.append("+")
    else:
        arrayResults.append("-")

    if (B > numberB):
        arrayResults.append("+")
    else:
        arrayResults.append("-")

    if (C > numberC):
        arrayResults.append("+")
    else:
        arrayResults.append("-")

    if (D > numberD):
        arrayResults.append("+")
    else:
        arrayResults.append("-")

    if (E > numberE):
        arrayResults.append("+")
    else:
        arrayResults.append("-")
    return arrayResults

def conclusionAboutTheWorkBlock(resultA,resultB,resultC,resultD,resultE):

    arrayBlocks=[]

    if(resultA=="-" and resultB=="-" and resultC=="-"):
        arrayBlocks.append("-")
    else:
        arrayBlocks.append("+")

    if (resultD == "-" and resultE == "-"):
        arrayBlocks.append("-")
    else:
        arrayBlocks.append("+")
    return arrayBlocks

def conclusionAboutTheWorkSystems(blockOne, blockTwo):
    if(blockOne == "+" and blockTwo == "+"):
        return "+"
    else:
        return "-"

def pStar(p_star_counter, numberOfTests):
    return round(p_star_counter/numberOfTests, 3)

def p1(A, B, C):
    return round(1-(1-A)*(1-B)*(1-C), 3)

def p2(D, E):
    return round(1-(1-D)*(1-E),3)

def p(p1, p2):
    return round(p1*p2,3)

def p_pStar(p, p_star):
    return round(abs(p-p_star),3)

