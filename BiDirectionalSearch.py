
import datetime
from PriorityQueue import PriorityMinQueue
from QueueNode import QueueNode


class BiDirectionalSearch:

    graph = {
        "s": [["u", 3], ["w", 5]],
        "u": [["v", 3]],
        "v": [["t", 3]],
        "w": [["t", 5]],
        "t": []
    }

    fParents = {}
    bParents = {}

    fNodeDis = {}
    bNodeDis = {}

    fQueue = [
        QueueNode("s"),
        QueueNode("u"),
        QueueNode("v"),
        QueueNode("w"),
        QueueNode("t")
    ]

    bQueue = [
        QueueNode("t"),
        QueueNode("u"),
        QueueNode("v"),
        QueueNode("w"),
        QueueNode("s")
    ]

    fHandles = {
        "s": 0,
        "u": 1,
        "v": 2,
        "w": 3,
        "t": 4
    }

    bHandles = {
        "t": 0,
        "u": 1,
        "v": 2,
        "w": 3,
        "s": 4
    }

    def getNbrsForBackSearch(self,node):
        list=[]
        for key,value in self.graph.items():
            for row in value:
                if row[0]==node:
                    list.append([key,row[1]])
        return list

    def main(self):
        self.fQueue[0].key = 0
        self.bQueue[0].key = 0

        self.fNodeDis.setdefault("s", 0)
        self.bNodeDis.setdefault("t", 0)

        fPQ=PriorityMinQueue(5,self.fQueue,self.fHandles)
        bPQ=PriorityMinQueue(5,self.bQueue,self.bHandles)
        print(datetime.datetime.now())

        while(fPQ.size> 0 or bPQ.size>0):

            meetingNode =fPQ.getMin().node
            if self.fNodeDis.get(bPQ.getMin().node) is  None  and self.bNodeDis.get(fPQ.getMin().node) is  None:

                # farword direction serach 

                fMin=fPQ.delete_min()
                self.fNodeDis.setdefault(fMin.node,fMin.key)
                if(fPQ.size!=0):


                    for nbrs in self.graph.get(fMin.node):
                        if self.fNodeDis.get(nbrs[0]) is None:

                            dis = self.fNodeDis.get(fMin.node) + nbrs[1]
                            index=fPQ.handles.get(nbrs[0])

                            if dis < fPQ.queue[index].key:
                                fPQ.queue[index].key=dis
                                self.fParents.setdefault(nbrs[0],fMin.node)
                                fPQ.heap_up(index)

                # backward direction search
                bMin=bPQ.delete_min()
                self.bNodeDis.setdefault(bMin.node,bMin.key)
                if(bPQ.size!=0):
                    for nbrs in self.getNbrsForBackSearch(bMin.node):

                        if self.bNodeDis.get(nbrs[0]) is None:
                            dis =self.bNodeDis.get(bMin.node) + nbrs[1]
                            index=bPQ.handles.get(nbrs[0])

                            if dis < bPQ.queue[index].key:
                                bPQ.queue[index].key=dis
                                self.bParents.setdefault(nbrs[0],bMin.node)
                                bPQ.heap_up(index)
            else:
                break
        print(datetime.datetime.now())
        print ("Shortest distance from S to T : " + str( fPQ.getMin().key + self.bNodeDis.get(meetingNode) ))

          
bidirectional=BiDirectionalSearch()
bidirectional.main()
print("done !")






