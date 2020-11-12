# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, depth = [(root, 1)], 0
        while stack:
            cur, cur_depth = stack.pop()
            if cur:
                depth = max(depth, cur_depth)
                if cur.left:
                    stack.append((cur.left, cur_depth+1))
                if cur.right:
                    stack.append((cur.right, cur_depth+1))
        return depth
