""" 
Build Suffix Tree data structure using arrays

 ["ana","ann","anna","anne"]

 banana

"""

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TrieNode:

    def __init__(self):
        self.list=[None]*27

class Data:
    def __init__(self,lable) -> None:
        self.label=lable
        self.children=TrieNode()

class Trie:

    lrs=''
    text=''

    def __init__(self) -> None:
        self.rootNode=TrieNode()

    def getIndex(self,char):
       
        return ord(char)-96
    

    def inorderTravesal(self,node:TrieNode):
        for item in node.list:
            if item !=None:
                if item.label[0] =='$':
                    print(item.label[0])
                else:
                    self.inorderTravesal(item.children)
                    print(item.label)

    def inorder2(self,node:TrieNode):
        for item in node.list:
            if item !=None:
                if item.label[0] =='$':
                   print(item.label[0:])
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

        data=Data('$'+"-"+str(index))
       
        data.children=None
        next.list[0]=data

    def search(self,keyword,node):
        for char in keyword:
            idx=self.getIndex(char)
            data=node.list[idx]
            if data!=None:
                node=data.children
            else:
                return False
        return True
    
    def inorderTravesalForAllOc(self,node:TrieNode,idxs:list):
        for item in node.list:
            if item !=None:
                if item.label[0] =='$':
                    idx=item.label.split("-")[1]
                    idxs.append(idx)
                else:
                    self.inorderTravesalForAllOc(item.children,idxs)
                   
    def findAllOccurances(self,keyword,node):
        isFound=True
        for char in keyword:
            idx=self.getIndex(char)
            data=node.list[idx]
            if data!=None:
                node=data.children
            else:
                isFound= False
                break
        if isFound:
            idxs=[]
            self.inorderTravesalForAllOc(node,idxs)
            return idxs
        else:
            return []
        
    def insertitionToFindLongestRepeatedSubString(self,text,idx):
        next=self.rootNode
        for char in text:
            idx=self.getIndex(char)
            data=next.list[idx]
            if data==None:
                next.list[idx]=Data(char)
            next=next.list[idx].children
        data=Data('$'+'-'+str(idx)+'-'+str(len(text)))
        data.children=None
        next.list[0]=data

    def longestRepeatedSubString(self,node):
        isDollar=False
        onePlusLeaves=False
        for child in node.list:
            if child!=None:
                if child.label[0]=='$':
                    isDollar=True
                else:
                    if isDollar:
                        onePlusLeaves=True
                    self.longestRepeatedSubString(child.children)
        
        if isDollar and onePlusLeaves:
            length=len(self.lrs)
            arrys=node.list[0].label.split("-")
            if length<int(arrys[2]):
                length=int(arrys[2])
                idx=int(arrys[1])
                self.lrs=self.text[idx:(idx+length)]
        


def main():
        text = "abcabcacab"
        tr=Trie()
        tr.text=text
        list=[]
        for i in range(len(text)):
            list.append(text[i:])
        print(list)

        # tr.longestRepeatedSubString(tr.rootNode)
        # print(tr.lrs )

       
if __name__=='__main__':
    main()


    




    









        
    









        



