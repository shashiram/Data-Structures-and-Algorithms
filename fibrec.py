


dic ={}

def getNthNum(n):

    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 2
    else :

        if (n-1) not in dic:
            dic[n-1]=getNthNum(n-1)
        if (n-2) not in dic:
            dic[n-2]=getNthNum(n-2)


        return (dic[n-1] + dic[n-2])

print (getNthNum(1000))

