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
    # My answer. Faster than Solution 2.
    longest: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node) -> int:
            path_l, path_r = 0, 0
            if node.left:
                left = dfs(node.left)
                if node.left.val == node.val:
                    path_l = left
            if node.right:
                right = dfs(node.right)
                if node.right.val == node.val:
                    path_r = right
            self.longest = max(self.longest, path_l + path_r)
            return max(path_l, path_r)+1
        if root is None:
            return 0
        dfs(root)
        return self.longest


class Solution2:
    # book answer. We can make 2 variables less than solution 1.
    longest: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
                # set path_l only when the value is same
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
                # set path_r only when the value is same
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.longest = max(self.longest, left+right)
            return max(left, right)
        dfs(root)
        return self.longest

