from bottle import post, request, template
import pdb 
import random
import pandas as pd
import json

@post('/program_mcm_3_2_A', method='post')
def my_form():

    #taking values from a form
    A_str=request.forms.get('NUMBER_A')
    B_str=request.forms.get('NUMBER_B')
    C_str=request.forms.get('NUMBER_C')
    D_str=request.forms.get('NUMBER_D')
    E_str=request.forms.get('NUMBER_E')
    N_str=request.forms.get('NUMBER_N')

    #conversion to numeric values
    A=float(A_str)
    B=float(B_str)
    C=float(C_str)
    D=float(D_str)
    E=float(E_str)
    numberOfTests=int(N_str)

    #class for filling in a table row
    class Rectangle():
        #designer
        def __init__(self):
            #initialization random values of elements
            self.numberA=round(random.uniform(0,1), 2)
            self.numberB=round(random.uniform(0,1), 2)
            self.numberC=round(random.uniform(0,1), 2)
            self.numberD=round(random.uniform(0,1), 2)
            self.numberE=round(random.uniform(0,1), 2)

            #initialization values of elements after comparison
            self.resultA = ""
            self.resultB = ""
            self.resultC = ""
            self.resultD = ""
            self.resultE = ""
            self.conclusionAboutTheWorkElement()

            #initializing block results
            self.blockOne = ""
            self.blockTwo = ""
            self.conclusionAboutTheWorkBlock()

            #initialization of the system operation result
            self.systems = ""
            self.conclusionAboutTheWorkSystems()

        #function-conclusion about the operation of the elements
        def conclusionAboutTheWorkElement(self):
            if(A > self.numberA):
                self.resultA = "+"
            else:
                self.resultA = "-"

            if (B > self.numberB):
                self.resultB = "+"
            else:
                self.resultB = "-"

            if (C > self.numberC):
                self.resultC = "+"
            else:
                self.resultC = "-"

            if (D > self.numberD):
                self.resultD = "+"
            else:
                self.resultD = "-"

            if (E > self.numberE):
                self.resultE = "+"
            else:
                self.resultE = "-"

        #function-conclusion about the operation of the blocks
        def conclusionAboutTheWorkBlock(self):
            if(self.resultA=="-" and self.resultB=="-" and self.resultC=="-"):
                self.blockOne = "-"
            else:
                self.blockOne = "+"

            if (self.resultD == "-" and self.resultE == "-"):
                self.blockTwo = "-"
            else:
                self.blockTwo = "+"

        #function-conclusion about the operation of the system
        def conclusionAboutTheWorkSystems(self):
            if(self.blockOne == "+" and self.blockTwo == "+"):
                self.systems = "+"
            else:
                self.systems = "-"

    list = []
    #filling the list with objects of the class
    for number in range(numberOfTests):
        rectangle = Rectangle()
        list.append(rectangle)

    p_star = 0
    p_star_counter = 0

    #counting the number of properly working systems
    for number in range(numberOfTests):
        if(list[number].systems == "+"):
            p_star_counter=p_star_counter+1

    #calculations of all major indicators
    p_star = p_star_counter/numberOfTests
    p1 = 1-(1-A)*(1-B)*(1-C)
    p2 = 1-(1-D)*(1-E)
    p = p1*p2
    p_pStar = abs(p-p_star)

    #creating a table header by columns
    df = pd.DataFrame(columns=['Test number'
                               ,'Block'
                               ,'Random number A'
                               ,'Random number B'
                               ,'Random number C'
                               ,'Random number D'
                               ,'Random number E'
                               ,'Element A'
                               ,'Element B'
                               ,'Element C'
                               ,'Element D'
                               ,'Element E'
                               ,'Work of blocks'
                               ,'Work of systems'
                               ])
    #df=df.set_index('Test number')

        #filling in the table with the first block
        df=df.append({
            'Test number':number+1
            ,'Block':"First"
            ,'Random number A':list[number].numberA
            ,'Random number B':list[number].numberB
            ,'Random number C':list[number].numberC
            ,'Random number D':""
            ,'Random number E':""
            ,'Element A':list[number].resultA
            ,'Element B':list[number].resultB
            ,'Element C':list[number].resultC
            ,'Element D':""
            ,'Element E':""
            ,'Work of blocks':list[number].blockOne
            ,'Work of systems':list[number].systems
            }, ignore_index=True)

        #filling in the table with the second block
        df=df.append({
            'Test number':""
            ,'Block':"Second"
            ,'Random number A':""
            ,'Random number B':""
            ,'Random number C':""
            ,'Random number D':list[number].numberD
            ,'Random number E':list[number].numberE
            ,'Element A':""
            ,'Element B':""
            ,'Element C':""
            ,'Element D':list[number].resultD
            ,'Element E':list[number].resultE
            ,'Work of blocks':list[number].blockTwo
            ,'Work of systems':""
            }, ignore_index=True)

    #conversion to the appropriate extension
    html=df.to_html()

    #create file and fill in it
    with open('mcm_3_2.html', 'a', encoding="utf-8") as outfile:
        outfile.write(template('template_saving_ak'
                    , A_str=A_str
                    , B_str=B_str
                    , C_str=C_str
                    , D_str=D_str
                    , E_str=E_str
                    , N_str=N_str
                    , p_star=p_star
                    , p1=p1
                    , p2=p2
                    , p=p
                    , p_pStar=p_pStar
                    , html=html))

    #returning the template
    return template('template_ak'
                    , A_str=A_str
                    , B_str=B_str
                    , C_str=C_str
                    , D_str=D_str
                    , E_str=E_str
                    , N_str=N_str
                    , p_star=p_star
                    , p1=p1
                    , p2=p2
                    , p=p
                    , p_pStar=p_pStar
                    , html=html,
                    button_back='/mcm_system_reliability_3_2')