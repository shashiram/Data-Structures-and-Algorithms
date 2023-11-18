

class Solution:

      memo=None
      p_memo=None

      def longestPalindrome(self, s: str) -> str:
            
            self.memo={}
            self.p_memo={}
            return self.fun(s,0,len(s)-1)
      def fun(self,given,i,j):
                  key=given[i:j+1] 
                  print(key)
                  if key in self.memo:
                        return self.memo.get(key)

                  p_str=''
                  if self.isP(given,i,j):
                        p_str=given[i:j+1]
                  
                  if p_str=='':
                        ch_1=self.fun(given,i,j-1)
                        ch_2=self.fun(given,i+1,j)
                        if len(ch_1)>len(ch_2):
                              p_str=ch_1
                        else:
                              p_str=ch_2

                  self.memo[key]=p_str
                  return    p_str 


      def isP(self,given,i,j):
                  
                  key=given[i:j+1] 

                  if key in self.p_memo:
                        return self.p_memo.get(key)
                  
                  if i==j:
                        self.p_memo[key]=True
                        return True
                  if i+1==j:
                        if given[i]==given[j]:
                              self.p_memo[key]=True
                              return True
                        else:
                              self.p_memo[key]=False
                              return False
                  else:
                        if given[i]!=given[j]:
                              self.p_memo[key]=False
                              return False
                        else:
                           rel= (given[i]==given[j]) and self.isP(given,i+1,j-1)
                           self.p_memo[key]=rel
                           return rel
            

sl=Solution()

kk=sl.longestPalindrome("whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone")

print(kk)

            