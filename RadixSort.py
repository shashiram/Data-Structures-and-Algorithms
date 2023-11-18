""" 

    list = {  }

    bb => 11= 1*26 +1 => 27
    a  => 0 => 0
    ba => 1*26+0 => 26
    b => 1=> 1
    abc => 1*26+2=> 2
"""
import math


class Data:
    def __init__(self,div,mod,num):
        self.key=mod
        self.div=div
        self.num=num
    
class RadixSort:
    givenList:list
    m=0
    base=256
    totalDigits=0
    def main(self,inputList):
        n=len(inputList)
        max_num=max(inputList)
        self.totalDigits=math.floor(math.log(max_num,self.base)) +1
        self.m=max(n,max_num)

        for i in range(len(inputList)):
            ele=inputList[i]
            list=divmod(ele,self.base)
            inputList[i]=Data(list[0],list[1],ele)

        self.givenList=inputList

        self.radixSort()

        for ele in self.givenList:
            print(ele.num,end=' ')

    def radixSort(self):
        
        for i in range(self.totalDigits):
            if i==0:
                self.countingSort()
            else:
                for i in range(len(self.givenList)):
                    ele=self.givenList[i]
                    list=divmod(ele.div,self.base)
                    ele.div=list[0]
                    ele.key=list[1]
                    self.givenList[i]=ele
                self.countingSort()

    
    def countingSort(self):

        countList=[0 for i in range(self.m+1)]
        for ele in self.givenList:
            countList[ele.key]=countList[ele.key]+1
        
        temp=self.m
        i=self.m
        while i>=0:
            countList[i]=temp-countList[i]
            temp=countList[i]
            i=i-1

        outList=[None for i in range(self.m+1)]
        for ele in self.givenList:
            outList[countList[ele.key]]=ele
            countList[ele.key]=countList[ele.key]+1

        sortList=[]
        for ele in outList:
            if ele!=None:
                sortList.append(ele)
                
        self.givenList=sortList
     


rd=RadixSort()

list=[97, 24929, 98] 
print(list)

rd.main(list)

        



    





        




        





    

        


        





