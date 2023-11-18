
# Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in 
# the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

# Input: N = 5, arr[] = {1, 101, 2, 3, 100} 
# Output: 106
# Explanation:The maximum sum of a
# increasing sequence is obtained from
# {1, 2, 3, 100}

given = [1,2,3]
memo={}
def fun (i):
    key=str(i)
    if key in memo:
        return memo.get(key)

    sum=given[i]
    if i==len(given)-1:
        memo[key]=sum
        return sum
    else:
        j=i+1
        while j< len(given):

            if given[i]< given[j]:
                sum_temp= given[i]+fun(j)
                if sum_temp>sum:
                    sum=sum_temp
            j+=1
        memo[key]=sum
        return sum

max_val=0
i=0

max_val_dic={}
max_val_dic['val']=0
max_val_dic['index']=None
            

while i<len(given):
    temp= fun(i)
    if max_val_dic.get('val')<temp:

        max_val_dic['val']=temp
        max_val_dic['index']=i

        max_val=temp
    i+=1


print(max_val_dic)

    
