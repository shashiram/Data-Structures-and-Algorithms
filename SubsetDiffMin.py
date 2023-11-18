


""" 
Partition a set into two subsets such that the difference of subset sums is minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements,
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 

Algo :

s1 + s2 =s (for dis joint sets)
s1=s-s2

diff=s1 - s2=s1-(s-s1)= 2*s1-s


dp( i,amt) = abs( min of ( dp(i+1), dp(i+1,s-2*s1)) )

"""
import math

given=[20, 19, 18, 20 ,16]

sum=0
for i in range(len(given)):
    sum=sum+given[i]


memo={}

def dp(i, target):
   
    key=hash((i,target))
    if key in memo:
        return memo.get(key)
    print(i,target)

    if i>=len(given):
        memo[key]=abs(target)
        return abs(target)
    else:
        min_val=min (dp(i+1,target),dp(i+1,target-2*given[i]))
        memo[key]=abs(min_val)
        return abs(min_val)
    
print(dp(0,sum))
print(memo)
