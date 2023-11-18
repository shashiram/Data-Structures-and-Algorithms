""" 

"""


class data:
    def __init__(self,key,type):
        self.key=key
        self.type=type


given=[3,1,5,6,0,0,0,0]
n=len(given)

m=max(n,max(given))
countList=[0 for i in range(m+1)]

for item in given:
    countList[item]=countList[item]+1

# in place diff list
temp=m
i=m
while i>=0:
    countList[i]=temp-countList[i]
    temp=countList[i]
    i=i-1

out=[None for ele in range(m+1)]

for i in range(n):
    ele=given[i]
    out[countList[ele]]=ele
    countList[ele]=countList[ele]+1

sortList=[]
for item in out:
    if item!=None:
        sortList.append(item)

print(sortList)

  







  







            
        








    






