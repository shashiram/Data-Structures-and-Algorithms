
given_str='character'

memo={}

def fun (i,j):

    key=str(i)+'_'+str(j)

    if key in memo:
        return memo.get(key)
    
    print(i,end='--')
    print(j)
    if i==j:
        memo[key]=given_str[i]
        return given_str[i]
    elif given_str[i]==given_str[j]:
        if i+1==j:
            ch=given_str[i]+given_str[j]
            memo[key]=ch
            return ch
        else:
            tem=given_str[i]+ fun(i+1,j-1) +given_str[j]
            memo[key]=tem
            return tem
    else:
        ch_1=fun(i,j-1)
        ch_2=fun(i+1,j)
        if len(ch_1)<len(ch_2):
            memo[key]=ch_2
            return ch_2
        else:
            memo[key]=ch_1
            return ch_1



print(fun(0,len(given_str)-1))
