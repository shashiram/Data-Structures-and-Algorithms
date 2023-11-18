
import datetime
import sys
from unicodedata import bidirectional
from PriorityQueue import PriorityMinQueue
from QueueNode import QueueNode




class Dijkstra:

    def main():
        parents = {}
        nodeSdis = {}
        graph = {
            "s": [["u", 3], ["w", 5]],
            "u": [["v", 3]],
            "v": [["t", 3]],
            "w": [["t", 5]],
            "t": []
        }

        queue = [
            QueueNode("s"),
            QueueNode("u"),
            QueueNode("v"),
            QueueNode("w"),
            QueueNode("t"),
        ]

        queue[0].key = 0

        handles = {
            "s": 0,
            "u": 1,
            "v": 2,
            "w": 3,
            "t": 4
        }

        nodeSdis.setdefault("s", 0)

        priorityMinQueue = PriorityMinQueue(5, queue, handles)

        print(datetime.datetime.now())

        while (priorityMinQueue.size > 0):


            min = priorityMinQueue.delete_min()
            nodeSdis.setdefault(min.node, min.key)
           
            if priorityMinQueue.size !=0:

                for nbrs in graph.get(min.node):
                    if nodeSdis.get(nbrs[0]) is None:
                        dis = nodeSdis.get(min.node) + nbrs[1]
                        index = priorityMinQueue.handles.get(nbrs[0])

                        if priorityMinQueue.queue[index].key > dis:
                            priorityMinQueue.queue[index].key = dis
                            parents.setdefault(nbrs[0], min.node)

                            priorityMinQueue.heap_up(index)
        print(datetime.datetime.now())
        for item in nodeSdis.items():
            print(item)

        print(" S---> T :"+ str( nodeSdis.get("t")))  
    main()      

