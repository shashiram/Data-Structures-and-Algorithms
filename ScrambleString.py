
"""
    We can scramble a string s to get a string t using the following algorithm:

        If the length of the string is 1, stop.
        If the length of the string is > 1, do the following:
        Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
        Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
        Apply step 1 recursively on each of the two substrings x and y.
        Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.


        Input: 

        s1 = "great", 
        s2 = "rgeat"

        Output: true

        Explanation: One possible scenario applied on s1 is:
        "great" --> "gr/eat" // divide at random index.
        "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
        "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
        "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
        "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
        "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
        The algorithm stops now, and the result string is "rgeat" which is s2.
        As one possible scenario led s1 to be scrambled to s2, we return true.

"""

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo={}
        LEN=len(s1)-1
        if len(s1)==1 :
            if s1==s2:
                return True
            else:
                return False
        def dp(i,j,p,q):
            
            key=hash((i,j,p,q))
            if key in memo:
                return memo[key]
            
            if i==j and p==q:
                if s1[i]==s2[p]:
                    memo[key]=True
                    return True
                else: 
                    memo[key]=False     
                    return False
            if (i+1==j) and (p+1==q):
                rt_val=(s1[i]==s2[p] and s1[j]==s2[q]) or (s1[i]==s2[q] and s1[j]==s2[p])
                memo[key]=rt_val
                return rt_val
            else :
                rt_val=False
                k=1
                len=(j-i) +1
                while k<len:
                    k_index=k-1
                    if  (dp(i,i+k_index,p,p+k_index) and dp(i+k_index+1,j,p+k_index+1,q)) or (dp(i,i+k_index,q-k_index,q) and dp(i+k_index+1,j,p,q-k_index-1)):
                        rt_val=True
                        break
                    k+=1
                memo[key]=rt_val
                return rt_val

        return dp(0,LEN,0,LEN)
    
sl=Solution()
s1="great"
s2="rgeat"

print(sl.isScramble(s1,s2))
