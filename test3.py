from typing import Optional

"""
[5,2,null,4,3,1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self) -> int:
        node5 = TreeNode(5)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node2 = TreeNode(2, node4, node5)
        root = TreeNode(1, node2, node3)

        parent = {root: None}
        sourceNodes = []

        fronts = [root]
        rootLevel = 0

        while len(fronts) > 0:
            newFronts = []
            for node in fronts:
                if node.left is not None:
                    newFronts.append(node.left)
                    parent[node.left] = node
                if node.right is not None:
                    newFronts.append(node.right)
                    parent[node.right] = node

                if node.left is None and node.right is None:
                    sourceNodes.append(node)
            if len(newFronts) > 0:
                rootLevel = rootLevel + 1
            fronts = newFronts

        maxVal = rootLevel
        for snode in sourceNodes:
            visited = {}
            level = 0
            frontiers = [snode]
            while len(frontiers) > 0:
                newFrontiers = []
                for node in frontiers:
                    visited[node] = True

                    if node.left is not None and node.left not in visited:
                        newFrontiers.append(node.left)
                    if node.right is not None and node.right not in visited:
                        newFrontiers.append(node.right)
                    if parent[node] is not None and parent[node] not in visited:
                        newFrontiers.append(parent[node])

                if len(newFrontiers) > 0:
                    level = level + 1
                frontiers = newFrontiers
            maxVal = max(maxVal, level)
        print(maxVal)


sl = Solution()
sl.diameterOfBinaryTree()
