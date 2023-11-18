

expression="7+4*9+5*6+8*2+1"
result_str="7+4*9"
memo={}

def fun(i,j):
    node=str(i)+"---"+str(j)

    if memo.get(node) is not None:
        print("memo")
        return memo.get(node)
    print("i---j :" +node)
    if i==(j-1):
        return int(expression[i])
    k=i+1
    max_temp=0
    while k< j:

        left_val_temp=fun(i,k)
        right_val_temp=fun(k+1,j)
        opt_val_temp=0
        if expression[k]=='*':
            opt_val_temp=left_val_temp*right_val_temp
        if expression[k]=='+':
            opt_val_temp=left_val_temp+right_val_temp
        if max_temp<opt_val_temp:
            max_temp=opt_val_temp
        k=k+2
    
    memo[node]=max_temp
    return max_temp

max_r=0
k=1
n=len(expression)
max_r=fun(0,n)
print(max_r)











