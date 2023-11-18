
""" 



"""

import math
n=5

matrix=[[0]*n for _ in range(n)]

dic={'key':0}


def fun(i,j,col,row):
        p=i
        q=j
        while q<col:
              dic['key']=dic['key']+1
              matrix[p][q]=dic['key']
              q+=1
        q=q-1
        p=p+1
        while p<row:
              dic['key']=dic['key']+1
              matrix[p][q]=dic['key']
              p+=1
        p=p-1
        q=q-1
        while q>=j:
              dic['key']=dic['key']+1
              matrix[p][q]=dic['key']
              q-=1
        q=q+1
        p=p-1
        while p>i:
               dic['key']=dic['key']+1
               matrix[p][q]=dic['key']
               p-=1

mid=0
if n%2==0:
    mid=(n/2)-1
else:    
  mid=math.floor(n/2)
k=0

while k<=mid :
      fun(k,k,n-k,n-k)
      k+=1
print(matrix)




               
              
        

    



