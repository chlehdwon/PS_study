"""
Given a binary tree, you need to compute the length of the diameter of
the tree. The diameter of a binary tree is the length of the longest
path between any two nodes in a tree. This path may or may not pass
through the root.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # dfs for left and right until leaf node
            left = dfs(node.left)
            right = dfs(node.right)

            # longest path
            self.longest = max(self.longest, left + right + 2)
            # status value
            return max(left, right) + 1

        dfs(root)
        return self.longest
