"""
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
prices = [7,1,5,3,6,4]

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxVal = prices[n - 1] - prices[n - 2] if (prices[n - 1] - prices[n - 2]) > 0 else 0
        maxId = (n - 1) if prices[n - 1] > prices[n - 2] else (n - 2)
        i = n - 3
        while i >= 0:
            tem = prices[maxId] - prices[i]
            if tem < 0:
                maxId = i
            else:
                if tem > maxVal:
                    maxVal = tem
            i = i - 1

        return(maxVal)

