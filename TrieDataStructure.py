
class TrieNode:

    def __init__(self) -> None:
        self.children={}
        self.eow=False

class Trie:

    def __init__(self) -> None:
        self.root=None

    def insert(self,key):

        next=self.root
        for i in range(len(key)):

            if self.root==None:
                self.root=TrieNode()
                new_node=TrieNode()
                self.root.children[key[i]]=new_node
                next=new_node
            else:

                if key[i] not in next.children:
                    new_node=TrieNode()
                    next.children[key[i]]=new_node
                    next.eow=False
                    next=new_node
                else:
                    next=next.children.get(key[i])

        next.eow=True

    def search(self,key):

        is_found=True

        next=self.root

        for i in range(len(key)):

            if key[i] not in next.children:
                is_found=False
                break
            else:
                if (next.children.get(key[i]).eow) and i<len(key)-1:
                    is_found=False
                    break    
                next=next.children.get(key[i])
        
        return is_found
    
    # def inprderTravesal(self,root):
 

    #     if node==None:
    #         print(node)
    #     else:

    #         print(root.children.keys())

    #         self.inprderTravesal(root.root.children)
    
      

def main():
     keys = ["ana","ann","anna","anne"]
     ts=Trie()
     for i in range(len(keys)):
         ts.insert(keys[i])

 
     print(ts.search("sha"))
     print(ts.search("m"))
         


if __name__=='__main__':
    main()










