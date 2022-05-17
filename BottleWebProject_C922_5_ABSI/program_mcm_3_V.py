from bottle import post, request, template
from numpy.core.numeric import False_
import pandas as pd
import random, math

@post('/mcm_estimating_failure_probilities_3', method='post')
def my_form():

    #application service time
    t1 = request.forms.get('NUMBER_t1')
    # the time for which applications need to be serviced
    t2=request.forms.get('NUMBER_t2')
    # exponential law distribution parameter
    a=request.forms.get('NUMBER_a')
    # number of tests
    n=request.forms.get('NUMBER_N')

    # converting from string to numbers
    t1=float(t1)
    t2=float(t2)
    a=float(a)
    n=int(n)
    all_tests=int(n)

    if t1>t2:
        return "hfhhfhf"

    n1=0
    flag=0
    ti=0.0
    link=[t1,0.0,0.0]
    count_test=1
    count=0
    # example to check
    #random_number=[0.1,0.09,0.73,0.25,0.33,0.76,0.52,0.01,0.35,0.86,0.34,0.67,0.35,0.48,0.76,0.8,0.95,0.9,0.91,0.17]
    number_of_requests_served=0
    count_1=0
    all_numbers_of_requests_served=[0]*n
    result=0

    # header of the test results output table
    df1=pd.DataFrame(columns=['xi','Requests served'])
   
    # table header
    df = pd.DataFrame(columns=['N test','Random number ri','-ln ri','Time between two appilications','Moment applying',
                               'The 1 channel','The 2 channel','The 3 channel','Service','Rejection'])
    
    # filling in the first row of the results table
    df = df.append({'N test':count_test,'Random number ri':'','-ln ri':'','Time between two appilications':'',
                                    'Moment applying':'','The 1 channel':t1,'The 2 channel':'', 'The 3 channel':'',
                                    'Service':1,'Rejection':''}, ignore_index=True)
    # repeated as many times as the user specified              
    while n>0:
        # if the time of receipt of the application is less than the total time of execution of applications
        while ti<t2:
            # random number
            random_number=random.uniform(0,1) 
            # finding -ln(random_number)
            convert_number_to_ln=-math.log(random_number)
            # duration of time between two consecutive bids with numbers 
            ri=(1/a)*convert_number_to_ln
            # the moment of receipt of the application
            ti+=ri
            # number of tests
            count_test+=1
            # pass by number of channels (3)
            for i in range(len(link)):
                # if the time of receipt of the application is greater than the time of the end of 
                # service of one of the channels, the application is received on this channel
                if ti>link[i]:
                    # the time of the end of the application service = the time of receipt of the application + 
                    # the time of the application service
                    link[i]=ti+t1
                    # if the time of receipt of the application is less than the total time of execution of applications
                    if ti<t2:
                        number_of_requests_served+=1
                        # which channel served the application
                        count_column=i
                    else:
                        count_column=-1
                    break
                else:
                    count_column=-1

            # enter only the data of the first test into the table
            # filling in the table
            if flag==0:
                if count_column==0:
                    df = df.append({'N test':count_test,'Random number ri':round(random_number,3),'-ln ri':round(convert_number_to_ln,3),'Time between two appilications':round(ri,3),
                                        'Moment applying':round(ti,3),
                                        'The 1 channel':round(link[count_column],3),
                                        'The 2 channel':'', 
                                        'The 3 channel':'',
                                        'Service':1,'Rejection':''}, ignore_index=True)
                elif count_column==1:
                    df = df.append({'N test':count_test,'Random number ri':round(random_number,3),'-ln ri':round(convert_number_to_ln,3),'Time between two appilications':round(ri,3),
                                'Moment applying':round(ti,3),
                                'The 1 channel':'',
                                'The 2 channel':round(link[count_column],3), 
                                'The 3 channel':'',
                                'Service':1,'Rejection':''}, ignore_index=True)
                elif count_column==2:
                    df = df.append({'N test':count_test,'Random number ri':round(random_number,3),'-ln ri':round(convert_number_to_ln,3),'Time between two appilications':round(ri,3),
                                'Moment applying':round(ti,3),
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':round(link[count_column],3),
                                'Service':1,'Rejection':''}, ignore_index=True)
                elif count_column==-1:
                    df = df.append({'N test':count_test,'Random number ri':round(random_number,3),'-ln ri':round(convert_number_to_ln,3),'Time between two appilications':round(ri,3),
                                'Moment applying':round(ti,3),
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':'',
                                'Service':'','Rejection':1}, ignore_index=True)     

        # number of applications served in each trial
        all_numbers_of_requests_served[count_1]=number_of_requests_served+1
        n-=1
        n1+=1
        ti=0.0 
        flag=1
        # filling in the results table
        df1=df1.append({'xi':n1,'Requests served':all_numbers_of_requests_served[count_1]},ignore_index=True)
        count_1+=1
        link=[t1,0.0,0.0]
        number_of_requests_served=0

    # total number of applications served
    for i in range(len(all_numbers_of_requests_served)):
        result+=all_numbers_of_requests_served[i]

    # calculation of the arithmetic mean of the total number of applications served in each test 
    # (mathematical expectation of the number of applications served)
    result/=len(all_numbers_of_requests_served)
    
    # html table
    html_table_of_test=df1.to_html()
    html=df.to_html()

    return template('template_sv', number_mcm=3, time=t2, total_count=count_test, number_of_requests_served=all_numbers_of_requests_served[0],
                    all_tests=all_tests, result=round(result,3), html1=html_table_of_test, button_back='\mcm_estimating_failure_probilities_3',html=html)
