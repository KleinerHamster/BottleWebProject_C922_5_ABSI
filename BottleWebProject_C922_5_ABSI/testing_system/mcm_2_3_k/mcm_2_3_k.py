def system_work_count(a_probability_, b_probability_, c_probability_, d_probability_, e_probability_,n_):
    from math import fabs 
    n=n_
    a_random=0
    b_random=0
    c_random=0
    d_random=0
    e_random=0
    f=0
    #outfile=open('C:/Users/kamillabalaeva/source/repos/BottleWebProject_C922_5_ABSI/BottleWebProject_C922_5_ABSI/mcm_2_3_K.txt', 'r')
    a_probability=a_probability_
    b_probability=b_probability_
    c_probability=c_probability_
    d_probability=d_probability_
    e_probability=e_probability_
    array=[[0.78,	0.27,	0.18,	0.00,	0.47],
           [0.22,	0.79,	0.08,	0.61,	0.54],
           [0.32,	0.70,	0.97,	0.13,	0.28],
           [0.30,	0.24,	0.90,	0.13,	0.31],
           [0.40,	0.71,	0.19,	0.94,	0.28],
           [0.79,	0.86,	0.66,	0.22,	0.40],
           [0.11,	0.74,	0.30,	0.27,	0.85],
           [0.52,	0.95,	0.59,	0.44,	0.88],
           [0.82,	0.56,	0.27,	0.72,	0.09],
           [0.03,	0.50,	0.92,	0.61,	0.25],
           [0.85,	0.18,	0.22,	0.53,	0.48],
           [0.17,	0.13,	0.10,	0.67,	0.47],
           [0.37,	0.45,	0.88,	0.68,	0.67],
           [0.68,	0.39,	0.53,	0.82,	0.47],
           [0.82,	0.24,	0.53,	0.51,	0.85],
           [0.72,	0.23,	0.88,	0.19,	0.03],
           [0.95,	0.27,	0.70,	0.99,	0.37],
           [0.22,	0.78,	0.57,	0.23,	0.92],
           [0.33,	0.24,	0.85,	0.81,	0.90],
           [0.95,	0.03,	0.95,	0.24,	0.18],
           [0.18,	0.38,	0.04,	0.75,	0.36],
           [0.37,	0.48,	0.31,	0.48,	0.15],
           [0.15,	0.38,	0.68,	0.92,	0.61],
           [0.92,	0.05,	0.96,	0.77,	0.84],
           [0.04,	0.57,	0.67,	0.32,	0.57],
           [0.81,	0.39,	0.82,	0.34,	0.63],
           [0.56,	0.53,	0.05,	0.38,	0.51],
           [0.22,	0.84,	0.34,	0.70,	0.68],
           [0.62,	0.10,	0.28,	0.80,	0.59],
           [0.72,	0.68,	0.53,	0.96,	0.16],
           [0.07,	0.24,	0.43,	0.42,	0.66],
           [0.15,	0.02,	0.40,	0.86,	0.87],
            [0.37,	0.47,	0.72,	0.74,	0.94],
            [0.94,	0.97,	0.92,	0.11,	0.55],
            [0.86,	0.75,	0.86,	0.17,	0.22],
            [0.21,	0.25,	0.59,	0.92,	0.33],
            [0.24,	0.33,	0.05,	0.46,	0.07],
            [0.70,	0.11,	0.86,	0.60,	0.38],
            [0.26,	0.71,	0.49,	0.28,	0.54],
            [0.42,	0.21,	0.26,	0.09,	0.15],
            [0.86,	0.37,	0.71,	0.56,	0.20],
            [0.73,	0.59,	0.60,	0.95,	0.34],
            [0.17,	0.40,	0.60,	0.90,	0.02],
            [0.97,	0.73,	0.64,	0.13,	0.44],
            [0.80,	0.74,	0.41,	0.90,	0.06],
            [0.56,	0.03,	0.63,	0.45,	0.09],
            [0.92,	0.35,	0.09,	0.83,	0.79],
            [0.43,	0.41,	0.80,	0.55,	0.62],
            [0.43,	0.11,	0.83,	0.47,	0.50],
            [0.86,	0.99,	0.31,	0.80,	0.76],
            [0.77,	0.93,	0.55,	0.47,	0.13],
            [0.18,	0.83,	0.61,	0.03,	0.01],
            [0.85,	0.63,	0.37,	0.15,	0.16],
            [0.36,	0.94,	0.09,	0.82,	0.42],
            [0.16,	0.00,	0.56,	0.77,	0.88],
            [0.42,	0.68,	0.80,	0.12,	0.91],
            [0.83,	0.87,	0.01,	0.76,	0.44],
            [0.56,	0.55,	0.71,	0.62,	0.18],
            [0.95,	0.74,	0.01,	0.18,	0.82],
            [0.90,	0.89,	0.67,	0.67,	0.34],
            [0.97,	0.82,	0.40,	0.26,	0.07],
            [0.10,	0.92,	0.32,	0.72,	0.25],
            [0.37,	0.96,	0.27,	0.65,	0.64],
            [0.43,	0.85,	0.54,	0.72,	0.98],
            [0.36,	0.82,	0.58,	0.24,	0.40],
            [0.71,	0.14,	0.89,	0.94,	0.87],
            [0.80,	0.52,	0.41,	0.57,	0.89],
            [0.96,	0.48,	0.46,	0.55,	0.15],
            [0.08,	0.15,	0.38,	0.80,	0.93],
            [0.60,	0.11,	0.25,	0.15,	0.34],
            [0.40,	0.82,	0.29,	0.90,	0.77],
            [0.10,	0.33,	0.30,	0.54,	0.61],
            [0.67,	0.42,	0.19,	0.59,	0.78],
            [0.59,	0.44,	0.71,	0.23,	0.13],
            [0.49,	0.90,	0.37,	0.58,	0.79],
            [0.23,	0.86,	0.12,	0.02,	0.93],
            [0.52,	0.40,	0.52,	0.29,	0.86],
            [0.55,	0.83,	0.43,	0.03,	0.37],
            [0.69,	0.39,	0.78,	0.95,	0.91],
            [0.66,	0.94,	0.19,	0.76,	0.53]] 
    for i in range(0,n,1):
         a_random=array[i][0]
         b_random=array[i][1]
         c_random=array[i][2]
         d_random=array[i][3]
         e_random=array[i][4]
         if ((a_random<float(a_probability) or b_random<float(b_probability)) and ( c_random<float(c_probability) or d_random<float(d_probability) or e_random <float(e_probability))):
             print ((a_random<float(a_probability) or b_random<float(b_probability)) and ( c_random<float(c_probability) or d_random<float(d_probability) or e_random <float(e_probability)))
             f+=1
    return f



def function_P(a,b,c,d,e, n):
    f=system_work_count(a,b,c,d,e,n)
    return (f/n)
def f_P1(a_probability_, b_probability_):
    a_probability=a_probability_
    b_probability=b_probability_
    return (1-((1-float(a_probability))*(1-float(b_probability))))

def f_P2(c_probability_, d_probability_, e_probability_):
    c_probability=c_probability_
    d_probability=d_probability_
    e_probability=e_probability_
    return (1-((1-float(c_probability))*(1-float(d_probability))*(1-float(e_probability))))
def function_itog(a,b,c,d,e, n):
    from math import fabs 
    P=function_P(a,b,c,d,e,n)
    P1=f_P1(a,b)
    P2=f_P2(c,d,e)
    P_=P1*P2
    p_absolutly=round(fabs(P_-P), 4)
    return p_absolutly

    
