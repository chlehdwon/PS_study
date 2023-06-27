"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ
in height by no more than 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # my first answer.
    # It is very bad beacause we have to call recursively function twice.
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        gap = left - right
        if gap <= -2 or gap >= 2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1


class Solution2:
    # book's answer. time is reduced becuase it is more simple recursive.
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or \
                    abs(left - right) > 1:
                # if there is unbalanced height, keep return -1
                return -1
            return max(left, right) + 1
        return dfs(root) != -1
