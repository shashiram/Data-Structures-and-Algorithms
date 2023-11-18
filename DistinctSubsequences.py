

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.


    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from s.
    rabbbit
    rabbbit
    rabbbit

algo: 

    dp(i,j)

"""

from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len=len(s)
        t_len=len(t)
        @cache
        def dp(i,j):

            if (i>=t_len and j >=s_len ) or i>=t_len:  
                return 1
            if j >=s_len and i<t_len:
                return 0
            if  t[i]==s[j]:
                return dp(i+1,j+1) + (dp(i,j+1) if (j+1)<s_len else 0)
            else:
                return (dp(i,j+1) if (j+1)<s_len else 0)
        return dp(0,0)

    
        
sl =Solution()
s = "ddd"
t = "dd"
print(sl.numDistinct(s,t))





