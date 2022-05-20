# checking the correctness of the calculation of the time of receipt of applications
def moment_of_receipt_of_the_application(random_number, a, t1):
    import math
    convert_number_to_ln=-math.log(random_number)
    ri=(1/a)*convert_number_to_ln
    ti=round(t1+ri,3)
    return ti

# checking the calculation of the end time of channel maintenance by different channels
def filling_channel(list_link, ti, t1):
    for i in range(len(list_link)):
        if ti>=list_link[i]:
           list_link[i]=round(ti+t1,3) 
           break
    
    return list_link

# the application has been serviced or refused
def request_counter(list_link):
    for link in list_link:
        if link:
            return True
        else:
            return False

# checking the calculation of the mathematical expectation (the average value of all tests performed)
def check_result(list_result):
    a=0                                                                                                                                                                                                                                                                 
    for result in list_result:
        a+=result
    a/=len(list_result)

    return round(a,3)
