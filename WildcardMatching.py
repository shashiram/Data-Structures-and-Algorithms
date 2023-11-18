

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aawew", p = "*"
Output: true
Explanation: '*' matches any sequence.

"""

from datetime import datetime

class Solution:

    txt:str
    pat:str
    memo:dict
    isStar:bool

    def __init__(self):
        self.txt=''
        self.pat=''
        self.memo={}
        self.isStar=False

    


    def isMatch(self, st: str, pt: str) -> bool:
        if st=='' and pt=='':
            return True
        if pt=='':
            return False
        self.txt=st

        self.complie(pt)
        self.memo={}
        self.isStar=False

        return self.dp('',0,0)
    
    def complie(self,pt):
            pre_char=''
            self.pat=''
            for i in range(len(pt)):   
                if not (pt[i]=='*' and pre_char=='*'):
                        pre_char=pt[i]
                        self.pat=self.pat+pt[i]
 
    def dp(self,pre,i,j):

        key =hash((i,j,pre))
        if key in self.memo:
            return self.memo.get(key)
        
        if i< len(self.pat) and j < len(self.txt):

            if self.pat[i]=='*':
                rtval=self.dp('*',i+1,j)
                self.memo[key]=rtval
                return rtval
            elif self.pat[i]=='?':
                if pre =='*':
                    rtval=(self.dp('',i+1,j+1) or self.dp(pre,i,j+1)) if self.txt[j]!='' else self.dp(pre,i,j+1)
                    self.memo[key]=rtval
                    return rtval
                else:
                    rtval=self.dp(pre,i+1,j+1) if self.txt[j]!='' else False
                    self.memo[key]=rtval
                    return rtval

            else:
                if pre=='*':
                        rtval=(self.dp('',i+1,j+1) or self.dp(pre,i,j+1)) if self.pat[i]==self.txt[j] else self.dp(pre,i,j+1)
                        self.memo[key]=rtval
                        return rtval

                else:
                        rtval=self.dp(pre,i+1,j+1) if self.pat[i]==self.txt[j] else False
                        self.memo[key]=rtval
                        return rtval
        else:

            if i<len(self.pat):
                    rtval=self.dp('*',i+1,j) if self.pat[i]=='*' else False
                    self.memo[key]=rtval
                    return rtval
            if j< len(self.txt):
                rtval = True if pre=='*' else False
                self.memo[key]=rtval
                return rtval
            else:
                self.memo[key]=True
                return True

s="aab"
p="c*a*b"

sl =Solution()
time1=datetime.now() 
print(sl.isMatch(s,p))
print((datetime.now().microsecond - time1.microsecond)/1000)







