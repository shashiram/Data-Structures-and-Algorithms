""" 
Input:  txt[] = “THISISATESTTEXT”, pat[] = “TEST”
Output: Pattern found at index 10 
"""


import math

txt = 'aabaacaadaabaaba'
pat = 'aaba'


class RollingHash:
    def __init__(self,s,mod_num):
        self.BASE=256
        self.hash=0
        self.prime=mod_num
        n=len(s)-1
        self.seqLen=len(s)-1
        self.CONT=self.BASE**(self.seqLen+1)%self.prime
        self.preHash=0
        for c in s:
            self.preHash+=(ord(c)*self.BASE**n)
            n-=1

        self.hash=self.preHash%self.prime

    def getHash(self):
        return self.hash
    
    def slide(self,pre, new):

        self.hash=(self.hash* self.BASE - ord(pre) * self.CONT + ord(new)%self.prime )%self.prime



p_num=len(pat)

i=2

while i<= math.sqrt(p_num):

    if p_num%i==0:
        p_num+=1
        i=2
    else:
        i+=1



pRL=RollingHash(pat,p_num)

tRL=RollingHash(txt[:len(pat)],p_num)

list=[]

for i in range(len(txt) -len(pat)+1):

    if i==0: 
        if pRL.getHash()==tRL.getHash() and pat==txt[i:i+len(pat)]:
            list.append(i)
    else:
        

        pre=txt[i-1]
        new=txt[i+len(pat)-1]
        sub_str=txt[i:i+len(pat)]
        tRL.slide(pre,new)


        if pRL.getHash()==tRL.getHash() and pat==sub_str:
            list.append(i)


print(list)





        


        
        
        




        




















    










