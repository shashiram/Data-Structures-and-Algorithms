
# You are given N pairs of numbers. In every pair, the first number is always smaller than the second number.
# A pair (c, d) can follow another pair (a, b) if b < c. 
# Chain of pairs can be formed in this fashion. You have to find the longest chain which can be formed from the given set of pairs. 


# Input:
# N = 5
# P[] = {5  24 , 39 60 , 15 28 , 27 40 , 50 90}
# Output: 3
# Explanation: The given pairs are { {5, 24}, {39, 60},
# {15, 28}, {27, 40}, {50, 90} },the longest chain that
# can be formed is of length 3, and the chain is
# {{5, 24}, {27, 40}, {50, 90}}


given = [[5,24],[39,60],[15,28],[27,40],[50,90]]

memo={}

def dp(i):
   
    key =str(i)
    if key in memo:
        return memo.get(key)
    len_max=1
    for j in range(len(given)):
        if given[i][1]<given[j][0]:
            temp_len=1+dp(j)
            if temp_len>len_max:
                len_max=temp_len
    print(i)
    memo[key]=len_max
    return len_max

max_len=0

for i in range(len(given)):
    tmp=dp(i)
    max_len=max(max_len,tmp)

print(max_len)
        



    

    


    