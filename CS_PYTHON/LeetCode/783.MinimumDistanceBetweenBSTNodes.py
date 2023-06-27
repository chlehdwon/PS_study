"""
Given a Binary Search Tree (BST) with the root node root, return the
minimum difference between the values of any two different nodes in the
tree.
"""

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev: int = float('-inf')
    diff: int = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node):
            if node.left:
                dfs(node.left)
            if self.prev != float('-inf'):
                self.diff = min(self.diff, node.val - self.prev)
            self.prev = node.val
            if node.right:
                dfs(node.right)
            return self.diff

        dfs(root)
        return self.diff


class Solution2:
    prev = -sys.maxsize
    result = sys.maxsize

    # recursive inorder traversal comparison result 
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


class Solution3:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # iteration inorder traversal comparison result
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
