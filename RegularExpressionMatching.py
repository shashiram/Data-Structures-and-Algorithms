

""" 
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial). 

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

"""

from functools import cache


class Solution :
    
    def isMatch(self, s: str, p: str) -> bool: 

        memo={}

        def dp(i,j,nxt):
                
                key=(i,j,nxt)
                if key in memo:
                    return memo[key]

                if j>=0 and i<0:
                    memo[key]=False
                    return False
                if i<0 and j<0:
                    memo[key]=True
                    return True
            
                if p[i]=='*':
                    memo[key]= dp(i-1,j,True)
                    return memo[key]
                if p[i]=='.':
                    if nxt:
                        if i==0:
                            memo[key]=True
                            return True
                        memo[key]=(dp(i-1,j,False) if j<0 else dp(i-1,j,False) or  dp(i-1,j-1,False) or dp(i,j-1,True))
                        return  memo[key]
                    else:
                        memo[key]=False if j<0 else dp(i-1,j-1,False) 
                        return  memo[key]     
                else:
                    if j<0:
                        if nxt:
                            if i==0:
                                memo[key]=True
                                return True
                            else:
                                if (i-1)==0 and p[0]==s[0] and len(s)>1:
                                    memo[key]=True
                                    return True
                                memo[key]=dp(i-1,j,False)
                                return memo[key]   
                        else:
                            memo[key]=False
                            return False 
                    else:

                        if p[i]==s[j]:
                            if nxt:
                                memo[key]=dp(i-1,j,False) or dp(i-1,j-1,False) or  dp(i,j-1,True)
                                return   memo[key]
                            else:
                                memo[key]=dp(i-1,j-1,False)
                                return memo[key]
                                
                        else:
                            if nxt:
                                memo[key]=dp(i-1,j,False)
                                return memo[key]
                            else:
                                memo[key]=False
                                return False


        return dp(len(p)-1,len(s)-1,False)
        

sl=Solution()
s = "ab"
p = ".*c"
print(sl.isMatch(s,p))
