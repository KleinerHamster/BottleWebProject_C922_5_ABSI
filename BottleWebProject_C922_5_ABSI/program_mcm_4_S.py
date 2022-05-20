from bottle import post, request, template
import pandas as pd
import random, math

@post('/mcm_estimating_failure_probilities_4', method='post')
def my_form():

    #application service time
    t1 = request.forms.get('t1')
    # the time for which applications need to be serviced
    t2=request.forms.get('t2')
    # exponential law distribution parameter
    a=request.forms.get('a')
    # number of tests
    n=request.forms.get('n')

    # converting from string to numbers
    t1=float(t1)
    t2=float(t2)
    a=float(a)
    n=int(n)

    count_of_tests=n
    ti=0.0
    link=[t1,0.0,0.0,0.0]
    count=0
    number_of_requests_served=1
    count_1=0
    all_numbers_of_requests_served=[0]*n
    result=0
    total_count=0

   
    # example to check
    #random_number=[0.1,0.09,0.73,0.25,0.33,0.76,0.52,0.01,0.35,0.86,0.34,0.67,0.35,0.48,0.76,0.8,0.95,0.9,0.91,0.17]

    # header of the test results output table
    df1=pd.DataFrame(columns=['Count of tests', 'Result'])

    # table header
    df = pd.DataFrame(columns=['Random number ri','-ln ri','Time between two consecutive applications','The moment of receipt of the application Ti=T(i-1)+ri',
                               'The 1 channel','The 2 channel',
                               'The 3 channel','The 4 channel',
                               'Serviced applications','Bounce rate'])


    # filling in the first row of the results table
    df = df.append({'Random number ri':'','-ln ri':'','Time between two consecutive applications':'',
                                    'The moment of receipt of the application Ti=T(i-1)+ri':'',
                                    'The 1 channel':t1,
                                    'The 2 channel':'', 
                                    'The 3 channel':'',
                                    'The 4 channel':'',
                                    'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
    
    
    
    # repeated as many times as the user specified          
    while n>0:
        # if the time of receipt of the application is less than the total time of execution of applications
        while ti<t2:
            # random number
            random_number=round(random.uniform(0.001,1),3)
            # finding -ln(random_number)
            convert_number_to_ln=round(-math.log(random_number),3)
            # duration of time between two consecutive bids with numbers 
            ri=round((1/a)*convert_number_to_ln,3)
            # the moment of receipt of the application
            ti+=round(ri,3)
            # pass by number of channels (4)
            for i in range(len(link)):
                # if the time of receipt of the application is greater than the time of the end of 
                # service of one of the channels, the application is received on this channel
                if ti>=link[i]:
                    
                    # the time of the end of the application service = the time of receipt of the application + 
                    # the time of the application service
                    link[i]=round(ti+t1,3) 

                    # if the time of receipt of the application is less than the total time of execution of applications
                    if ti<t2:
                        

                        number_of_requests_served+=1
                        # which channel served the application
                        count_column=i
                    else:
                        count_column=-2
                    break
                elif ti>t2:
                    count_column=-2
                else:
                    count_column=-1

            # enter only the data of the first test into the table
            # filling in the table
            if count_of_tests==n:
                # total number of applications
                total_count+=1
                if count_column==0:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                        'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                        'The 1 channel':link[count_column],
                                        'The 2 channel':'', 
                                        'The 3 channel':'',
                                        'The 4 channel':'',
                                        'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
                elif count_column==1:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                'The 1 channel':'',
                                'The 2 channel':link[count_column], 
                                'The 3 channel':'',
                                'The 4 channel':'',
                                'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
                elif count_column==2:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':link[count_column],
                                'The 4 channel':'',
                                'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
                elif count_column==3:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':'',
                                'The 4 channel':link[count_column],
                                'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
                elif count_column==-1:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':'',
                                'The 4 channel':'',
                                'Serviced applications':'','Bounce rate':1}, ignore_index=True)     

                elif count_column==-2:
                    df = df.append({'Random number ri':random_number,'-ln ri':convert_number_to_ln,'Time between two consecutive applications':ri,
                                'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                'The 1 channel':'',
                                'The 2 channel':'', 
                                'The 3 channel':'',
                                'The 4 channel':'',
                                'Serviced applications':'','Bounce rate':'stop'}, ignore_index=True)     

            count+=1

        # number of applications served in each trial
        all_numbers_of_requests_served[count_1]=number_of_requests_served
        n-=1
        count_1+=1
        ti=0
        count=0
        number_of_requests_served=1
        link=[t1,0.0,0.0,0.0]

        

    
    # filling in the results table
    for i in range(len(all_numbers_of_requests_served)):
        df1=df1.append({'Count of tests':i+1, 'Result':all_numbers_of_requests_served[i]}, ignore_index=True)
        # total number of applications served
        result+=all_numbers_of_requests_served[i]

    # calculation of the arithmetic mean of the total number of applications served in each test 
    # (mathematical expectation of the number of applications served)
    result/=len(all_numbers_of_requests_served)

    # html table
    html_table_of_test=df1.to_html()
    html=df.to_html()

    #create file and fullfill it
    with open('mcm_4.html', 'a', encoding="utf-8") as outfile:
        outfile.write(template('template_saving_sv'
                    , t1=request.forms.get('t1')
                    , t2=request.forms.get('t2')
                    , a=request.forms.get('a')
                    , N=request.forms.get('n')
                    , number_mcm=4, time=t2, total_count=total_count, number_of_requests_served=all_numbers_of_requests_served[0]
                    , all_tests=count_of_tests-1, html1=html_table_of_test, result=round(result,3)
                    , html=html))

    return template('template_sv', number_mcm=4, time=t2, total_count=total_count, number_of_requests_served=all_numbers_of_requests_served[0],
                    all_tests=count_of_tests-1, html1=html_table_of_test, result=round(result,3), button_back='\mcm_estimating_failure_probilities_4',html=html)


