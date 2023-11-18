
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
# weight_fun=w*(level of key) for all i to j

given=[[1,1],[2,10],[3,8],[4,9]]

keys=[1,2,3,4]



def dp(i,j,l):

    if i==j:
        return (l+1)*given[i][1]
    else:

        k=i
        min_val=sys.maxsize
        while k<= j:

            root_weight =(l+1)*given[k][1]
            left_weight=dp(i,k-1,(l+1)) if (k-1)>= i else 0
            right_weight=dp(k+1,j,(l+1)) if (k+1)<=j else 0
            sum=root_weight+left_weight+right_weight
            
            min_val=min(min_val,sum)

            k=k+1
        return min_val



i=0
j=len(given)-1
k=i
min_val=sys.maxsize
while k<= j:
    root_weight =given[k][1]
    left_weight= dp(i,k-1,1) if (k-1)>= i else 0
    right_weight=dp(k+1,j,1) if (k+1)<=j else 0

    sum=root_weight+left_weight+right_weight
    min_val=min(min_val,sum)
    k=k+1

print(min_val)














          

          


    

