


import sys
class Solution:
    memo:dict
    def coinChange(self, coins, amount):
        self.memo={}
        return self.dp(coins,amount)

    def dp(self,coins,amount):

        if amount in self.memo:
            return self.memo.get(amount)
        print(amount)
        if amount==0:
            self.memo[amount]=0
            
            return 0
        if amount==coins[0]:
            self.memo[amount]=1
            return 1
        else:
            min_count=sys.maxsize
            for i in range(len(coins)):
                if coins[i]<=amount:
                    count=1+self.dp(coins,amount-coins[i])
                    if count>0:
                        min_count=min(count,min_count)
            if min_count==sys.maxsize:
                self.memo[amount]=-1
                return -1
            else:
                self.memo[amount]=min_count
                return min_count

coins= [ 6,9, 5, 1]
coins.sort(reverse=True)
total = 11        
sl=Solution()

print(sl.coinChange(coins,total))


            





