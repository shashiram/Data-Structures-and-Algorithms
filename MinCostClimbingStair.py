
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.




import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size



memo={}
cost =[841,462,566,398,243,248,238,650,989,576,361,126,334,729]

path={}

def fun(index):

    if memo.get(index) is not None:
       
        return memo.get(index)
    if index>=len(cost):
        return 0
    if index==len(cost)-1:
        return cost[index]
    if index==len(cost)-2:
        return cost[index]

    temp1=fun(index+1)
    temp2=fun(index+2)

    if temp1<temp2:
        path[index]=index+1
    else:
        path[index]=index+2


    memo[index]=cost[index] + min(temp1,temp2)
    return memo.get(index)


total_cost1=fun(0)
total_cost2=fun(1)
total_cost=min(total_cost1,total_cost2)
print(total_cost)

if total_cost1<total_cost2:
    index=0
else:
    index=1

clm_path=str(index)+'-'+str(cost[index])+'====>'

while path.get(index) is not None:
    
    clm_path=clm_path+str(path.get(index))+'-'+str(cost[index])+'====>'
    index=path.get(index)
clm_path=clm_path+'top'

print(clm_path)






   





