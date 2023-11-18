
str_temp = '0101'

def fun(i,j):

    if i>=len(str_temp) and j>=len(str_temp):
        return 0
    if i==len(str_temp)-1:
        if str_temp[i]==0:
            str_temp=str_temp[:i]+'1'+str_temp[i+1:]
            return 1
        else:
            return 0
    if str_temp[i]==str_temp[j]:
        str_temp=str_temp[:i]+'0'+str_temp[i+1:]
        str_temp=str_temp[:j]+'1'+str_temp[j+1:]
        return 1 +fun(i+1,j+1)
    else:
        if not (str_temp[i]==0 and str_temp[j]==1):
            str_temp=str_temp[:i]+'0'+str_temp[i+1:]
            str_temp=str_temp[:j]+'1'+str_temp[j+1:]
            return 1 +fun(i+1,j+1)
        return fun(i+1,j+1)
    
def fun1(i,j):

    if i>=len(str_temp) and j>=len(str_temp):
        return 0
    if i==len(str_temp)-1:
        if str_temp[i]==0:
            return 0
        else:
            str_temp=str_temp[:i]+'0'+str_temp[i+1:]
            return 1

    if str_temp[i]==str_temp[j]:
        str_temp=str_temp[:i]+'0'+str_temp[i+1:]
        str_temp=str_temp[:i]+'1'+str_temp[i+1:]
        return 1 +fun1(i+1,j+1)
    else:
        
        if not (str_temp[i]==1 and str_temp[j]==0):
            str_temp=str_temp[:i]+'1'+str_temp[i+1:]
            str_temp=str_temp[:j]+'1'+str_temp[j+1:]
            
            return 1 +fun1(i+1,j+1)
        return fun1(i+1,j+1)
    
min_val=min(fun(0,1),fun1(0,1))
print(min_val) 
    


    

