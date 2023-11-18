
class Solution:

    str_dic={}
    given_str=''
    memo={}

    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        self.given_str=s
        self.str_dic={'str':'','len':0}
        self.memo={}
        i=0
        j=len(s)-1
        self.fun(i,j)
        print(self.str_dic)
        return self.str_dic.get('str')

    def fun(self,i,j):
        subStr=self.given_str[i:j+1]

        if self.memo.get(subStr) is None:
            if len(subStr)==1:
                self.setDicValue(subStr)
                self.memo[subStr]=1
                return 1
            if self.isPlalind(subStr):
                self.memo[subStr]=len(subStr)
                return len(subStr)
            else:
                return max(self.fun(i,j-1),self.fun(i+1,j))

        else:
            return self.memo.get(subStr)

    def isPlalind(self,str):
        if str==str[::-1] :
            self.setDicValue(str)
            return True
        else:
         return False

    def setDicValue(self,str):
            if self.str_dic["str"]=="":
                self.str_dic["str"]=str
                self.str_dic["len"]=len(str)
            else:
                if self.str_dic["len"]<len(str):
                    self.str_dic["str"]=str
                    self.str_dic["len"]=len(str)

sl=Solution()
print(sl.longestPalindrome("abbcccbbbcaaccbababcbcabca"))

