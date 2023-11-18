""" 
Build Trie data structure using arrays

 ["ana","ann","anna","anne"]

 banana

"""

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TrieNode:

    def __init__(self):
        self.list=[None]*28

class Data:
    def __init__(self,lable) -> None:
        self.label=lable
        self.children=TrieNode()

class Trie:

    sortedList:list

    def __init__(self) -> None:
        self.rootNode=TrieNode()
        self.sortedList=[]

    def getIndex(self,char):
        if char=='$':
            return 1
        return ord(char)-95

    def inorder2(self,node:TrieNode):
        for item in node.list:
            if item !=None:
                if item.label[0] =='&':
                   for ele in item.label.split('-')[1].split('#'): 
                     self.sortedList.append(ele)
                  
                else:
                    self.inorder2(item.children)
                                      
    def insert(self,text,index):
        next=self.rootNode
        for char in text:
            idx=self.getIndex(char)
            data=next.list[idx]
            if data==None:
                next.list[idx]=Data(char)
            next=next.list[idx].children

        if next.list[0]==None:
            data=Data('&-'+str(index))
            data.children=None
            next.list[0]=data 
        else:
            next.list[0].label=next.list[0].label +'#'+str(index)

    def main(self,texts):

            for idx,text in enumerate(texts):
                self.insert(text,idx)

            self.inorder2(self.rootNode)




    




    









        
    









        



