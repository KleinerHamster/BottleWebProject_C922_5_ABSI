from bottle import post, request
import pandas as pd
import random, math

@post('/mcm_estimating_failure_probilities_4', method='post')
def my_form():

    # ����� ������������ ������
    t1 = request.forms.get('t1')
    # �����, �� ������� ����� ��������� ������
    t2=request.forms.get('t2')
    # �������� ������������� �������������� ������
    a=request.forms.get('a')
    # ���������� ����������� ���������
    n=request.forms.get('n')

    # ������� �� ������ � �����
    t1=float(t1)
    t2=float(t2)
    a=float(a)
    n=int(n)

    
    ti=0.0
    link=[t1,0.0,0.0,0.0]
    count=0
    # ������ ��� ��������
    random_number=[0.1,0.09,0.73,0.25,0.33,0.76,0.52,0.01,0.35,0.86,0.34,0.67,0.35,0.48,0.76,0.8,0.95,0.9,0.91,0.17]
    number_of_requests_served=0
    count_1=0
    all_numbers_of_requests_served=[0]*n
    result=0

    # ����� �������
    df = pd.DataFrame(columns=['Random number ri','-ln ri','Time between two consecutive applications ri=0.2(-ln ri)','The moment of receipt of the application Ti=T(i-1)+ri',
                               'The moment Ti+0.5 of the end of the application service by the 1 channel','The moment Ti+0.5 of the end of the application service by the 2 channel',
                               'The moment Ti+0.5 of the end of the application service by the 3 channel','The moment Ti+0.5 of the end of the application service by the 4 channel',
                               'Serviced applications','Bounce rate'])
    df = df.append({'Random number ri':'','-ln ri':'','Time between two consecutive applications ri=0.2(-ln ri)':'',
                                    'The moment of receipt of the application Ti=T(i-1)+ri':'',
                                    'The moment Ti+0.5 of the end of the application service by the 1 channel':t1,
                                    'The moment Ti+0.5 of the end of the application service by the 2 channel':'', 
                                    'The moment Ti+0.5 of the end of the application service by the 3 channel':'',
                                    'The moment Ti+0.5 of the end of the application service by the 4 channel':'',
                                    'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
                 
    while n>0:
        while ti<t2:
            # ��������� �����
            #random_number=random.uniform(0,1) 
            # ���������� -ln random_number
            convert_number_to_ln=-math.log(random_number[count])
            # ������������ ������� ����� ����� ����������������� �������� � �������� i-1 � i
            ri=(1/a)*convert_number_to_ln
            # ������ ����������� ������
            ti+=ri
            # ������ �� ���������� ������� (4)
            for i in range(len(link)):
                # ���� ������ ����������� ������ ������ ������� ��������� ������������ ������ �� �������, ������ ��������� �� ���� �����
                if ti>link[i]:
                    # ������ ��������� ������������ ������ = ������ ����������� ������ + ����� ������������ ������
                    link[i]=ti+t1
                    # ���������� ����������� ������
                    if ti<t2:
                        number_of_requests_served+=1
                        # ����� ����� ���������� ������
                        count_column=i
                    else:
                        count_column=-1
                    break
                else:
                    count_column=-1

            # ���������� ������� 
            if count_column==0:
                df = df.append({'Random number ri':random_number[count],'-ln ri':convert_number_to_ln,'Time between two consecutive applications ri=0.2(-ln ri)':ri,
                                    'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                                    'The moment Ti+0.5 of the end of the application service by the 1 channel':link[count_column],
                                    'The moment Ti+0.5 of the end of the application service by the 2 channel':'', 
                                    'The moment Ti+0.5 of the end of the application service by the 3 channel':'',
                                    'The moment Ti+0.5 of the end of the application service by the 4 channel':'',
                                    'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
            elif count_column==1:
                df = df.append({'Random number ri':random_number[count],'-ln ri':convert_number_to_ln,'Time between two consecutive applications ri=0.2(-ln ri)':ri,
                            'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                            'The moment Ti+0.5 of the end of the application service by the 1 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 2 channel':link[count_column], 
                            'The moment Ti+0.5 of the end of the application service by the 3 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 4 channel':'',
                            'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
            elif count_column==2:
                df = df.append({'Random number ri':random_number[count],'-ln ri':convert_number_to_ln,'Time between two consecutive applications ri=0.2(-ln ri)':ri,
                            'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                            'The moment Ti+0.5 of the end of the application service by the 1 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 2 channel':'', 
                            'The moment Ti+0.5 of the end of the application service by the 3 channel':link[count_column],
                            'The moment Ti+0.5 of the end of the application service by the 4 channel':'',
                            'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
            elif count_column==3:
                df = df.append({'Random number ri':random_number[count],'-ln ri':convert_number_to_ln,'Time between two consecutive applications ri=0.2(-ln ri)':ri,
                            'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                            'The moment Ti+0.5 of the end of the application service by the 1 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 2 channel':'', 
                            'The moment Ti+0.5 of the end of the application service by the 3 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 4 channel':link[count_column],
                            'Serviced applications':1,'Bounce rate':''}, ignore_index=True)
            elif count_column==-1:
                df = df.append({'Random number ri':random_number[count],'-ln ri':convert_number_to_ln,'Time between two consecutive applications ri=0.2(-ln ri)':ri,
                            'The moment of receipt of the application Ti=T(i-1)+ri':ti,
                            'The moment Ti+0.5 of the end of the application service by the 1 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 2 channel':'', 
                            'The moment Ti+0.5 of the end of the application service by the 3 channel':'',
                            'The moment Ti+0.5 of the end of the application service by the 4 channel':'',
                            'Serviced applications':'','Bounce rate':1}, ignore_index=True)     

            count+=1

        # ���������� ����������� ������ � ������ ���������
        all_numbers_of_requests_served[count_1]=number_of_requests_served
        n-=1
        count_1+=1

    # ���������� �������� ��������������� �� ������ ���������� ����������� ������ � ������ ���������
    for i in range(len(all_numbers_of_requests_served)):
        result+=all_numbers_of_requests_served[i]

    # �������������� �������� ����� ����������� ������ 
    result/=len(all_numbers_of_requests_served)

    # html �������
    html=df.to_html()

    return html




