from bottle import post, request, template
from bottle import SimpleTemplate
import json
#import pandas as pd
import random, math
from math import fabs
import pandas as pd
n=5
array=[]
@post('/mcm_system_reliability_2_3', method='post')
def my_form():
    a_probability=request.forms.get('A')
    b_probability=request.forms.get('B')
    c_probability=request.forms.get('C')
    d_probability=request.forms.get('D')
    e_probability=request.forms.get('E')
    array_probability=[float(a_probability),float(b_probability), float(c_probability), float(d_probability),float(e_probability)]
    data_frame=pd.DataFrame(columns=['#','Random number A','Random number B','Random number C', 'Random number D','Random number E','Block 1', 'Block 2', 'System'])
    a_random=0
    b_random=0
    c_random=0
    d_random=0
    e_random=0
    f=0
    c_system=''
    c_block_1=''
    c_block_2=''
    for i in range(0,n,1):
         a_random=round(random.random(), 2)
         b_random=round(random.random(),2)
         c_random=round(random.random(),2)
         d_random=round(random.random(),2)
         e_random=round(random.random(),2)
         if ((a_random<float(a_probability) or b_random<float(b_probability)) and ( c_random<float(c_probability) or d_random<float(d_probability) or e_random <float(e_probability))):
            c_system='+'
            c_block_1='+'
            c_block_2='+'
            f+=1
         elif (a_random<float(a_probability) or b_random<float(b_probability)):
             c_system='-'
             c_block_1='+'
             c_block_2='-'
         else:
             c_system='-'
             c_block_1='-'
             c_block_2='+'
         data_frame=data_frame.append({'#':i,'Random number A':float(a_random),'Random number B':float(b_random),'Random number C':float(c_random), 'Random number D':float(d_random),'Random number E':float(e_random),'Block 1':c_block_1, 'Block 2':c_block_2, 'System':c_system}, ignore_index=True)
         array.append([float(a_random),float(b_random),float(c_random), float(d_random),float(e_random),c_block_1, c_block_2, c_system])
    P=f/n
    P1=1-((1-float(a_probability))*(1-float(b_probability)))
    P2=1-((1-float(c_probability))*(1-float(d_probability))*(1-float(e_probability)))
    P_=P1*P2
    p_absolutly=round(fabs(P_-P), 4)
    html=data_frame.to_html()
    #запись в файл indent для более удобеого чтения записей
    with open('mcm_2_3_K.txt', 'a') as outfile:#открытие файла
        json.dump(array_probability, outfile)
        outfile.write("\n")
        json.dump(array, outfile)
        outfile.write("\n")
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

