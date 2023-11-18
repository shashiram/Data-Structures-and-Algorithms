

# Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of C = { C1, C2, .., Cm} 
# valued coins, what is the minimum number of coins to make the change? 
# If it’s not possible to make a change, print -1.

# Examples:

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents

import sys

coins=[5, 6, 9, 1]
total = 9

memo={}

def fun(amt):
    if amt in memo:
        return memo.get(amt)
    
    print(amt)
    if amt==0:
        memo[amt]=0
        return 0
    if amt==coins[0]:
        memo[amt]=1
        return 1
    else:
        min_coins=sys.maxsize
        i=0
        while i <len(coins):
            if coins[i]<=amt:
                sum=1+fun(amt-coins[i])
                if sum>0:
                    min_coins=min(min_coins,sum)
            
            
            i=i+1
        if min_coins==sys.maxsize:
            memo[amt]=-1
            return -1
        else :
            memo[amt]=min_coins
            return min_coins
        
print(fun(total))

print(memo)


            

            

              






    





