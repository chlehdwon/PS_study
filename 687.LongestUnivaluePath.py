"""
Given the root of a binary tree, return the length of the longest path,
where each node in the path has the same value. This path may or may not
pass through the root.

The length of the path between two nodes is represented by the number of
edges between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node) -> int:
            path_l, path_r = 0, 0
            if node.left:
                left, left_val = dfs(node.left)
                if left_val == node.val:
                    path_l = left
            if node.right:
                right, right_val = dfs(node.right)
                if right_val == node.val:
                    path_r = right
            self.longest = max(self.longest, path_l + path_r)
            return (max(path_l, path_r)+1, node.val)
        dfs(root)
        return self.longest

