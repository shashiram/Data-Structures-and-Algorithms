
str_1= "XXXXZY"
str2 ="XXY"
str3= "XXZ"




def fun(i,j,k):




    if i<len(str_1) and j<len(str2) and k<len(str3):

        c=str_1[i]
        if matchStr2(c,j):
            if c==str2[j]:
                return fun(i+1,j+1,k)
            else:
                return fun(i+1,j,k)
        elif matchStr3(c,k):
            if c==str3[k]:
                return fun(i+1,j,k+1)
            else:
                return fun(i+1,j,k)
        else:
            return False
    else:

        if i>=len(str_1) and j>=len(str2) and k>=len(str3):
            return True
        else:
            if i>=len(str_1):
                return False
            else:
                c=str_1[i]
                if j<len(str2):
                   
                    if matchStr2(c,j):
                        if c==str2[j]:
                            return fun(i+1,j+1,k)
                        else:
                            return fun(i+1,j,k)
                    else:
                        return False
                else:
                    if matchStr3(c,k):
                        if c==str3[k]:
                            return fun(i+1,j,k+1)
                        else:
                            return fun(i+1,j,k)
                    else:
                        return False

                    


def matchStr2(c,j):
    if j<0:
        return False
    if c==str2[j]:
        return True
    return matchStr2(c,j-1)

def matchStr3(c,k):
    if k<0:
        return False
    if c==str3[k]:
        return True
    return matchStr3(c,k-1)


                

