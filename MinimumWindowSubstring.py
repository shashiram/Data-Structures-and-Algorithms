"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""
from datetime import datetime

import test2


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = {}
        for char in t:
            if char in dicT:
                dicT[char] = dicT[char] + 1
            else:
                dicT[char] = 1
        p = None
        i = 0
        queue = LinkedList()
        cnt = len(t)
        minP = None
        minQ = None
        while i < len(s):

            if s[i] in dicT:
                if dicT[s[i]] > 0:
                    dicT[s[i]] = dicT[s[i]] - 1
                    cnt = cnt - 1
                    if cnt == 0:
                        queue.insert(i, s[i])
                        if p is None:
                            p = i
                        minP = p
                        minQ = i
                        break
                    else:
                        queue.insert(i, s[i])
                        if p is None:
                            p = i
                else:
                    if s[p] == s[i]:
                        idx = queue.deQueue(s[i])
                        if idx is None:
                            p = i
                        else:
                            p = idx
                        queue.insert(i, s[i])
                    else:
                        queue.deleteAndInsert(i, s[i])
            i += 1
        i += 1
        while i < len(s):
            if s[i] in dicT:
                if s[i] == s[p]:
                    p = queue.deQueue(s[i])
                    queue.insert(i, s[i])
                    if (i - p + 1) < (minQ - minP + 1):
                        minP = p
                        minQ = i
                else:
                    queue.deleteAndInsert(i, s[i])

            i = i + 1
        print(dicT)
        if minP is None or minQ is None:

            return ""
        else:
            return (s[minP:minQ + 1])


class Node:
    def __init__(self, key):
        self.pre = None
        self.nxt = None
        self.key = key


class InnerQueue:
    def __init__(self):
        self.head = None
        self.rear = None

    def insert(self, key):
        node = Node(key)
        if self.head is None:
            self.head = node
            self.rear = node
        else:
            node.pre = self.rear
            self.rear.nxt = node
            self.rear = self.rear.nxt

    def deleteHead(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.nxt
            if self.head is not None:
                self.head.pre = None
            else:
                self.rear = None
            return temp.key
        else:
            return None

    def getHead(self):
        return self.head


class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None
        self.dicMapData = {}

    def insert(self, key, char):
        node = Node(key)
        if self.head is None:
            self.head = node
            self.rear = node
        else:
            node.pre = self.rear
            self.rear.nxt = node
            self.rear = node

        innerQ = InnerQueue()
        if char in self.dicMapData:
            innerQ = self.dicMapData[char]
        innerQ.insert(node)
        self.dicMapData[char] = innerQ

    def delete(self, delNode):

        if self.head is not None and self.head.key == delNode.key:
            self.head = self.head.nxt
            if self.head is not None:
                self.head.pre = None
        elif self.rear is not None and self.rear.key == delNode.key:
            self.rear = self.rear.pre
            if self.rear is not None:
                self.rear.nxt = None
        else:
            if self.head is not None and self.rear is not None:
                pre = delNode.pre
                nxt = delNode.nxt
                nxt.pre = pre
                pre.nxt = nxt

    def deleteAndInsert(self, idx, char):
        if char in self.dicMapData:
            innerQ = self.dicMapData[char]
            delNode = innerQ.deleteHead()
            if innerQ.getHead() is None:
                self.dicMapData.pop(char)
            self.delete(delNode)
            self.insert(idx, char)
        else:
            self.insert(idx, char)

    def deQueue(self, char):
        if self.head is not None:
            innerQ = self.dicMapData[char]
            innerQ.deleteHead()
            if innerQ.getHead() is None:
                self.dicMapData.pop(char)
            else:
                self.dicMapData[char] = innerQ

            self.head = self.head.nxt
            if self.head is not None:
                self.head.pre = None
                return self.head.key
            else:
                self.rear = None
                return None


sl = Solution()
s = "ADOBEODEBANC"
t = "ABC"

print(sl.minWindow(s, t))

