


import math
import string


given_str='1214'



def delete_fun():

    count=0
    temp_str=given_str
    while len(temp_str)>0:
            max_len_str=fun(0,len(temp_str),temp_str)
            temp_str=temp_str.replace(max_len_str,'')
            count+=1

    return count




def fun(i,j,str_max):


    sub_str=str_max[i:j]

    print(sub_str)
    
    
    if isPalendrome(sub_str):
        return sub_str
    else:
        ch_1=fun(0,i+1,str_max)
        ch_2=fun(i+1,j,str_max)

        if(len(ch_1)<len(ch_2)):
            return ch_2
        else:
            return ch_1
        
    
def isPalendrome(sub_str):

    if len(sub_str)==1:
        return True
    else:
       if sub_str==sub_str[::-1]:
           return True
       else:
           False


print('delete required :'+ str(delete_fun()))





        




