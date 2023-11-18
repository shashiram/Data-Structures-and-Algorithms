

import math


given =[1,2,3]

sum=0
for i in range(len(given)):
    sum=sum+given[i]
t_sum=sum/2

index_dic={}

def fun(i,target):

    if i==len(given)-1:
        if given[i]<=target:
          
            return given[i]
        else:
            return 0
    else:
        index_dic[i]=False
        ch_1=fun(i+1,target)
        if target-given[i]>0:
            index_dic[i]=True
            ch_2=fun(i+1,target-given[i])+given[i]
            return max(ch_1,ch_2)
        else:
            
            return ch_1
   
returnVal=fun(0,t_sum)

set_1=[]
set_2=[]

if returnVal==t_sum:
    for key in index_dic.keys():
        if index_dic.get(key):
            set_1.append(given[key])
        else:
            set_2.append(given[key])

    print(True)
    print(set_1)
    print(set_2)

else:
    print(False)










    
       

     










    
    


