"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

     ex:
     Input: head = [1,2,3,4,5], k = 2
     Output: [2,1,4,3,5]


"""
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListCus:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur is not None:

                if cur.next is None:
                    break
                cur=cur.next
            cur.next=node
class Demo:

    def main(self):
        list = [1, 2, 3, 4, 5,6]
        k = 1
        passCnt = math.floor(len(list) / k)
        lnkd = LinkedListCus()
        for ele in list:
            lnkd.insert(ele)


        head = lnkd.head
        newHead = None
        bridgeNode = None

        for i in range(passCnt):
            tempBridgeNode = None
            preNode = None

            for j in range(k):
                if j == k-1:
                    if newHead is None:
                        newHead = preNode
                        bridgeNode = tempBridgeNode
                    else:
                        bridgeNode.next = preNode
                        bridgeNode = tempBridgeNode

                elif preNode is None:
                    tempHead = head
                    preNode = head.next
                    head = head.next.next
                    tempHead.next = None
                    preNode.next = tempHead
                    tempBridgeNode = tempHead

                else:
                    tempHead = head
                    head = head.next
                    tempHead.next = preNode
                    preNode = tempHead


        bridgeNode.next=head

        cur =newHead
        while cur is not None:
                print(cur.val)
                cur=cur.next

dm=Demo()
dm.main()


