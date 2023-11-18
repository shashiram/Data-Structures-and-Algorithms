"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Ex:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 42 + 465 = 807.

        l1 = [2, 4] => 42
        l2 = [5, 6, 4]=> 465
"""
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head: ListNode
        self.head = None

    def insert(self, val):
        node = ListNode(val)

        if self.head is None:
            self.head = node
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = node


class Demo:

    def __init__(self):
        self.head = None
        self.rear = None

    def main(self):
        l1 = [2,4,9]
        l2 =  [5,6,4,9]

        lnkd1 = LinkedList()
        lnkd2 = LinkedList()
        for ele in l1:
            lnkd1.insert(ele)

        for ele in l2:
            lnkd2.insert(ele)

        sum = lnkd1.head.val + lnkd2.head.val
        val = sum % 10
        node = ListNode(val)
        self.head = node
        self.rear = self.head

        carry = math.floor(sum / 10)
        h1 = lnkd1.head.next
        h2 = lnkd2.head.next

        while h1 is not None or h2 is not None:
            if h1 is not None and h2 is not None:
                carry = self.getCarry(h1.val + h2.val + carry)
                h1 = h1.next
                h2 = h2.next
            elif h1 is not None and h2 is None:
                carry = self.getCarry(h1.val + carry)
                h1 = h1.next
            else:
                carry = self.getCarry(h2.val + carry)
                h2 = h2.next

        if carry != 0:
            tempNode = ListNode(carry)
            self.rear.next = tempNode
            self.rear = self.rear.next

        curNode = self.head

        while curNode is not None:
            print(curNode.val)
            curNode = curNode.next

    def getCarry(self, sum):
        val = sum % 10
        tempNode = ListNode(val)
        carry = math.floor(sum / 10)
        self.rear.next = tempNode
        self.rear = self.rear.next
        return carry


dm = Demo()
dm.main()
