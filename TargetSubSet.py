

given=[2,5,7,8,9]
target=400

def fun(i, target):

    if i==len(given) and target==0:
        return True
    elif i==len(given) and target>0:
        return False
    else:

        cho=fun(i+1,target)
        if((target-given[i])>=0):
            cho1=fun(i+1,target-given[i])
            return cho or cho1 
        return cho
        



    
