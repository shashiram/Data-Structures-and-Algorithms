

# str 1 to str 2

str1="shashiram"
str2="shashi"

dictemp={}


def fun(i,j):
        
        return_val=0
        key=str(i)+str(j)

        if key in dictemp:
              print(key)
              return dictemp.get(key)

        if (i >=len(str1)) and (j>=len(str2)):
             return return_val
        else:
               if (i<len(str1)) and (j<len(str2)):
                      if str1[i]==str2[j]:
                             return_val=fun(i+1,j+1)
                      else:
                             return_val = min(1+fun(i,j+1),1+fun(i+1,j+1),1+fun(i+1,j))
                             
               else:
                    
                    if i <len(str1):
                        return_val= 1+fun(i+1,j)

                    else: 
                        return_val= 1+fun(i,j+1)


        dictemp[key]=return_val
        return return_val

print(fun(0,0))


        


















