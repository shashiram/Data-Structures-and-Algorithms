
import sys


class QueueNode:
    key=sys.maxsize
    node=None
    def __init__(self,node):
        self.node=node
        