from bottle import post, request
from bottle import SimpleTemplate
#import pandas as pd
import random, math
f=0
from math import fabs
n=100

@post('/mcm_system_reliability_2_3', method='post')
def my_form():
    a_probability=request.forms.get('A')
    b_probability=request.forms.get('B')
    c_probability=request.forms.get('C')
    d_probability=request.forms.get('D')
    e_probability=request.forms.get('E')


    a_random=0
    b_random=0
    c_random=0
    d_random=0
    e_random=0
    f=0
    for i in range(0,n,1):
         a_random=random.random()
         b_random=random.random()
         c_random=random.random()
         d_random=random.random()
         e_random=random.random()
         if ((a_random<float(a_probability) or b_random<float(b_probability)) and ( c_random<float(c_probability) or d_random<float(d_probability) or e_random <float(e_probability))):
             f+=1
    P=f/n
    return "P=%s" %P

