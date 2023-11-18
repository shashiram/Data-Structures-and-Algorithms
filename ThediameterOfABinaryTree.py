"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
[5,2,null,4,3,1]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2)
root = TreeNode(1, node2)


def fun(node: TreeNode):
    if node.left is None and node.right is None:
        return [0, 0]
    elif node.left is None and node.right is not None:
        right = fun(node.right)
        pathMax = 1 + right[1]
        maxVal = max(right[0], 1 + right[1])
        return [maxVal, pathMax]

    elif node.left is not None and node.right is None:
        left = fun(node.left)
        pathMax = 1 + left[1]
        maxVal = max(left[0], 1 + left[1])
        return [maxVal, pathMax]
    else:

        left = fun(node.left)
        right = fun(node.right)

        pathMax = 1 + max(left[1], right[1])

        maxVal = max(left[0], right[0], 2 + left[1] + right[1])

        return [maxVal, pathMax]


print(fun(root)[0])



