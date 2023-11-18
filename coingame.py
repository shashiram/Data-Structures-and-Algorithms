

given_coins=[5,10,100,25]

n=len(given_coins)

i=0
j=n-1

plays=['I','Y']

list={}

def fun(i,j,p):


    if p=='I':

        op1=given_coins[i]
        op2=given_coins[j]

        if not ((i+1)>j):
            op1=op1 +fun(i+1,j,'Y')

        if not ((j-1)<i):
            op2=op2+fun(i,j-1,'Y')
        
        if op1>op2:
            list[given_coins[i]]='I'
        if op2>op1:
            list[given_coins[j]]='I'
        return max(op1,op2)



    else:
          op1=0
          op2=0
          if not ((i+1)>j):
             op1=fun(i+1,j,'I')
          if not ((j-1)<i):
             op2=fun(i,j-1,'I')

          if op1>op2:
            list[given_coins[i]]='Y'
          if op2>op1:
            list[given_coins[j]]='Y'
          return min(op1,op2);

        

print (fun(i,j,'I'))
print(list)



      



