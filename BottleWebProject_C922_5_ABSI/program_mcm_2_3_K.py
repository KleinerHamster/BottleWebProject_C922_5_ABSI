from bottle import post, request, template
from bottle import SimpleTemplate
import json
#import pandas as pd
import random, math
from math import fabs
import pandas as pd
#initialization  of array
array=[]
#function to calculate the probability of faultless operation of the first unit
def f_P1(a_probability, b_probability):
    a_probability_=a_probability
    b_probability_=b_probability
    return (1-((1-float(a_probability_))*(1-float(b_probability_))))
#function to calculate  the probability of faultless operation of the second unit
def f_P2(c_probability, d_probability, e_probability):
    c_probability_=c_probability
    d_probability_=d_probability
    e_probability_=e_probability
    return (1-((1-float(c_probability_))*(1-float(d_probability_))*(1-float(e_probability_))))
#processed the method 
@post('/mcm_system_reliability_2_3', method='post')
def my_form():
    a_probability=request.forms.get('A')#getting data from users
    b_probability=request.forms.get('B')
    c_probability=request.forms.get('C')
    d_probability=request.forms.get('D')
    e_probability=request.forms.get('E')
    n=request.forms.get('n')
    n=int(n)
    #recording of user data in an array for convenient formation in a file
    array_probability=[float(a_probability),float(b_probability), float(c_probability), float(d_probability),float(e_probability)]
    data_frame=pd.DataFrame(columns=['#','Random number A','Random number B','Random number C', 'Random number D','Random number E','Block 1', 'Block 2', 'System'])
    a_random=0
    b_random=0
    c_random=0
    d_random=0
    e_random=0
    f=0
    #initialization of character variables for further beautiful display in the table
    c_system=''
    c_block_1=''
    c_block_2=''
    #Start cycle to compare the values with random for PW calculation
    for i in range(0,n,1):
         a_random=round(random.random(), 2)
         b_random=round(random.random(),2)
         c_random=round(random.random(),2)
         d_random=round(random.random(),2)
         e_random=round(random.random(),2)
         #system validation
         if ((a_random<float(a_probability) or b_random<float(b_probability)) and ( c_random<float(c_probability) or d_random<float(d_probability) or e_random <float(e_probability))):
            c_system='+'#system work
            c_block_1='+'#block1 work
            c_block_2='+'#block2 work
            f+=1#counter on non-functional system
         elif (a_random<float(a_probability) or b_random<float(b_probability)):
             c_system='-'#system do not work
             c_block_1='+'#system work
             c_block_2='-'#systemdo not work
         else:
             c_system='-'#system do not work
             c_block_1='-'#system do not work
             c_block_2='+'#system work
             #adding intermediate data to the table
         data_frame=data_frame.append({'#':i,'Random number A':float(a_random),'Random number B':float(b_random),'Random number C':float(c_random), 'Random number D':float(d_random),'Random number E':float(e_random),'Block 1':c_block_1, 'Block 2':c_block_2, 'System':c_system}, ignore_index=True)
         #adding intermediate data to the array for further convenient formation in a file
         array.append([float(a_random),float(b_random),float(c_random), float(d_random),float(e_random),c_block_1, c_block_2, c_system])
    #P - system reliability assessment
    P=f/n
    #finding the probability of faultless operation of first and second blocks
    P1=f_P1(a_probability,b_probability)
    P2=f_P2(c_probability, d_probability, e_probability)
    #finding the probability of faultless operation of the system
    P_=P1*P2
    #finding absolute error
    p_absolutly=round(fabs(P_-P), 4)
    #table formatting in html format
    html=data_frame.to_html()
    with open('mcm_2_3.html', 'a',encoding="utf-8") as outfile:
        outfile.write(template( 'template_saving_ak'#writing template to html file
                    , A_str=a_probability
                    , B_str=b_probability
                    , C_str=c_probability
                    , D_str=d_probability
                    , E_str=e_probability
                    , N_str=n
                    , p_star=P
                    , p1=P1
                    , p2=P2
                    , p=P_
                    , p_pStar=p_absolutly
                    , html=html))

    return template('template_ak'
                    , A_str=a_probability
                    , B_str=b_probability
                    , C_str=c_probability
                    , D_str=d_probability
                    , E_str=e_probability
                    , N_str=n
                    , p_star=P
                    , p1=P1
                    , p2=P2
                    , p=P_
                    , p_pStar=p_absolutly
                    , html=html,
                     button_back='/mcm_system_reliability_2_3')
