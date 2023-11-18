
givePins=[1,-3,9,1]
n =len(givePins)
subMax=None
i=n-1

def pinMax(i):
    if i==n-1:
        return givePins[i]
    else:
        if (i+1)<n:
            return max(givePins[i],givePins[i]*givePins[i+1],subMax)
        else:
            return max(givePins[i],subMax)

while i>=0:
    
    subMax=pinMax(i)
    i=i-1

print(subMax)

