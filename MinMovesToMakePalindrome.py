from datetime import datetime
class ListNode:
    def __init__(self, data: int):
        self.data = data
        self.nxt = None
        self.pre = None


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.h = 0
        self.min = data
        self.max = data


class LinkedList:
    head: ListNode
    rear: ListNode

    def __init__(self):
        self.head = None
        self.rear = None

    def insert(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            self.rear = node
        else:
            node.pre = self.rear
            self.rear.nxt = node
            self.rear = self.rear.nxt

    def deleteAtRear(self):
        if self.rear.pre is None:
            self.rear = None
            self.head = None
        else:
            self.rear = self.rear.pre
            self.rear.nxt = None

    def deleteAtFront(self):
        if self.head.nxt is None:
            self.head = None
            self.rear = None
        else:
            self.head = self.head.nxt
            self.head.pre = None


class BST:
    root: BSTNode

    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = BSTNode(data)
        if self.root is None:
            self.root = newNode
        else:
            self.find(self.root, newNode)

    def find(self, node: BSTNode, newNode: BSTNode):

        if newNode.data < node.data:
            if node.left is None:
                newNode.parent = node
                node.left = newNode
                self.balanceTree(newNode)
            else:
                self.find(node.left, newNode)
        else:
            if node.right is None:
                newNode.parent = node
                node.right = newNode
                self.balanceTree(newNode)
            else:
                self.find(node.right, newNode)

    def balanceTree(self, node: BSTNode):

        if not (node is None or node.parent is None):
            parent = node.parent
            right_h = (-1 if parent.right is None else parent.right.h)
            left_h = (-1 if parent.left is None else parent.left.h)

            parent_skew = right_h - left_h
            if parent_skew == 2:
                node_skew = (-1 if node.right is None else node.right.h) - (-1 if node.left is None else node.left.h)
                if node_skew == -1:
                    self.rightRotation(node)
                self.leftRotation(parent)
            elif parent_skew == -2:
                node_skew = (-1 if node.right is None else node.right.h) - (-1 if node.left is None else node.left.h)
                if node_skew == 1:
                    self.leftRotation(node)
                self.rightRotation(parent)
            else:
                parent.h = 1 + max(right_h, left_h)
                right_size = (0 if parent.right is None else parent.right.size)
                left_size = (0 if parent.left is None else parent.left.size)
                parent.size = 1 + right_size + left_size

                if parent.left is not None and parent.left.data == node.data:
                    parent.min = node.min
                else:
                    parent.max = node.max

            self.balanceTree(parent)

    def leftRotation(self, node: BSTNode):
        right = node.right
        parent = node.parent

        node.right = right.left
        if right.left is not None:
            node.right.parent = node
        right.left = node
        node.parent = right
        right.parent = parent

        if parent is not None:
            if parent.right is not None and parent.right.data == node.data:
                parent.right = right
            else:
                parent.left = right
        else:
            self.root = right

        node.h = 1 + max((-1 if node.right is None else node.right.h), (-1 if node.left is None else node.left.h))
        node.size = 1 + (0 if node.right is None else node.right.size) + (0 if node.left is None else node.left.size)
        node.min = node.data if node.left is None else node.left.min
        node.max = node.data if node.right is None else node.right.max

        right.h = 1 + max((-1 if right.right is None else right.right.h), (-1 if right.left is None else right.left.h))
        right.size = 1 + (0 if right.right is None else right.right.size) + (
            0 if right.left is None else right.left.size)
        right.min = right.data if right.left is None else right.left.min
        right.max = right.data if right.right is None else right.right.max

    def rightRotation(self, node: BSTNode):
        left = node.left
        parent = node.parent

        node.left = left.right
        if left.right is not None:
            node.left.parent = node
        left.right = node
        node.parent = left
        left.parent = parent

        if parent is not None:
            if parent.right is not None and parent.right.data == node.data:
                parent.right = left
            else:
                parent.left = left
        else:
            self.root = left

        node.h = 1 + max((-1 if node.right is None else node.right.h), (-1 if node.left is None else node.left.h))
        node.size = 1 + (0 if node.right is None else node.right.size) + (0 if node.left is None else node.left.size)
        node.min = node.data if node.left is None else node.left.min
        node.max = node.data if node.right is None else node.right.max

        left.h = 1 + max((-1 if left.right is None else left.right.h), (-1 if left.left is None else left.left.h))
        left.size = 1 + (0 if left.right is None else left.right.size) + (
            0 if left.left is None else left.left.size)
        left.min = left.data if left.left is None else left.left.min
        left.max = left.data if left.right is None else left.right.max

    def rightSidedQuery(self, node: BSTNode, key):
        if node is None:
            return 0
        if key < node.data:
            if node.left is None or key > node.left.max:
                return 1 + (0 if node.right is None else node.right.size)
            else:
                return 1 + (0 if node.right is None else node.right.size) + self.rightSidedQuery(node.left, key)
        else:
            return self.rightSidedQuery(node.right, key)

    def rangeQuery(self, node, key1, key2):
        if node is None:
            return 0
        if key2 < self.root.min or self.root.max < key1:
            return 0
        else:
            return self.rightSidedQuery(node, key1) - self.rightSidedQuery(node, key2)


class Solution:
    def minMovesToMakePalindrome(self, st: str) -> int:
        s = st
        occursDic = {}
        for i in range(len(s)):
            if s[i] in occursDic:
                linkedObj = occursDic[s[i]]
                linkedObj.insert(i)
            else:
                linkedObj = LinkedList()
                linkedObj.insert(i)
                occursDic[s[i]] = linkedObj
        i = 0
        j = len(s) - 1
        bst = BST()
        moves = 0
        visit = {}
        setMid = False
        while not (i == j or i > j):

            if i not in visit and j not in visit:

                if i == occursDic[s[i]].rear.data:
                    setMid = True
                char = s[j] if setMid else s[i]
                lnkObj = occursDic[char]
                occurIndex = lnkObj.head.data if setMid else lnkObj.rear.data
                if occurIndex == i or occurIndex == j:
                    if setMid:
                        visit.setdefault(j)
                    else:
                        visit.setdefault(i)
                    i = i + 1
                    j = j - 1
                else:
                    visitCnt = bst.rangeQuery(bst.root, i, occurIndex) if setMid else bst.rangeQuery(bst.root,
                                                                                                     occurIndex, j)

                    moves += (occurIndex - i - visitCnt) if setMid else (j - occurIndex - visitCnt)
                    bst.insert(occurIndex)
                    if setMid:
                        j = j - 1
                    else:
                        i = i + 1
                visit.setdefault(occurIndex)
                lnkObj.deleteAtRear()
                lnkObj.deleteAtFront()
            else:
                if i in visit:
                    i = i + 1
                else:
                    j = j - 1
        return moves


sl = Solution()
time1 = datetime.now()
print(sl.minMovesToMakePalindrome(
    "orbazgoyxaovdyzuhcgrygyuxobgktiidypdcxdzcmxnluxgbuxpibzitmpxnprukpsemjmlufakyltltqwguovlrmvfjtldkluilducurigwxxzccxkrikicalxbgyjtvgwmvxdnchafvmnxjuvdmxyyghftvriuuhxmcelfyapgcucrotoaecwwbgpqqbragpjdzxdhvxytibfoblpvotkgqewjbzvlndbkcvudbqkxnhzxnfwmqbavhzcbktnaqvfjarippmdrxxsthjdgjeyqjhklhozradujcvochdatfjougejwcainqrpemsbntnhektjbdvvukxbtafysmuljibjwwznsiroryarpwjdlfvhbvwejevxdxiyxpseixzppqfzuldunftcvgrdsmwdsieqzjwjuqrmyyxupaxqffruozuzfaiiddhyzsnwaxflkjugazjhzgeaatnynakzregvdlpozhsiqrjvahrkfdedbtdyrboavvuyiuuuwzgiscvavazazwdarckimtwkqhnojbqcbjowyhcxeycfgtiredpducbpezolkvnygraabbirkpmkrdapfekrpiydfofrytrnnrumiuciaedrrhxrmtxycwyowemctcfznehayxdrsgmtwdtyjxvuloraajugjtfallfrtlxzlvgpyvyxdqgenwulrjlyoyazportbypclnrxhrrohqnvjcydevxcjvxmmdxbgdjxfkwaohwikwgllrfwfffhawsrzejezexlrabwefrdewkmqifcyxxcqtecyqbrwfwpgqxtdkqtcikwmlutrnijchkkqyzkpvvgaywnfwydojooilbonukplajcrocgtwaegxrrqwsakmygmcvuqqdberojoxypzccbbcejxghruwtyhbwyanxahuffwqssycduowrrujwntnsxnrnpyatwlxdohywvbhwuuatoxwvzgmfunaxfluptfmqewstvyhzmzzaykhmrdkymddwjmxtjyudwfchqhvjspeyybzvbakscvwweekvxdwgriodpjtxtnwcqjuowqrxglszsqkznstvrdmzuzvkugrtnukqxjihnyopngxxjfhtsfagvcdhanwqfggtcgznejcaacuuxkqoagujetbhnvmoctwklnotaymibnysitnsddkcoezkawltdmlrgugtbrgdgapqwvmfrjnhzhghohlchkzzytawevizsptkpbjcuvmeiccdionxzspsrbwhwrydcaqhjjdkwcqvjkrtmxjpwvdxolpjmujlsgiadpwsfvmjpfuyhcdowjeexlmlwfdqmpmhdkuvntsotasodlpeqebnacgaexzuedmotnwrpaupnyyuokuapmqoamcjghmmtfjhrtboufdqkusryqdvwwndfuzootadcowrqqrdafvacxszxwpyjsyhgcceczlekvfquyhupagwdlzyttvnphuylajzqftdskkvojzbqawsphvozkpzxlbbdwpgdpzatgbtjtcsexzwqautwptxlfrwvkacugybsnpjklwqygczndotgajgpwaswacpocvrctnflrnbtnpqcqesoydzvohjmmvwryorfdrvonyhhhyxzzdbjhxosxwpmbrwubryyiozliulzzwjjhqlmezgwttakowwcuvgwmruplvnoixyxhbtlplvodkoscotrjyvnpgdqtvcrysrsudbftrgrmrbdstvqlcghbeupohfzutwplqssqpqqsdicgjqfhwsycjufanpouwhyquqtrcdoeakqxqjmgfhrdghaowtzoyfvveivzmdabbttqatuznxfkqejepcvyjdztfnyikdirsaukpqhrdgnfftc"))
print((datetime.now().microsecond - time1.microsecond) / 1000)