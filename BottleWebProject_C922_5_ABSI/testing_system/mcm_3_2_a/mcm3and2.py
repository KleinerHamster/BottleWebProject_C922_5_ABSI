#The function of concluding on the operation of all elements
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

#The function of concluding the operation of all blocks
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

#The function of the conclusion about the operation of the system
def conclusionAboutTheWorkSystems(blockOne, blockTwo):
    if(blockOne == "+" and blockTwo == "+"):
        return "+"
    else:
        return "-"

#Function relative frequency calculation
def pStar(p_star_counter, numberOfTests):
    return round(p_star_counter/numberOfTests, 3)

#Function calculation of the probability of failure-free operation of the first block
def p1(A, B, C):
    return round(1-(1-A)*(1-B)*(1-C), 3)

#Function calculation of the probability of failure-free operation of the second block
def p2(D, E):
    return round(1-(1-D)*(1-E),3)

#Function calculation of system reliability
def p(p1, p2):
    return round(p1*p2,3)

#Function calculation of absolute error
def p_pStar(p, p_star):
    return round(abs(p-p_star),3)

