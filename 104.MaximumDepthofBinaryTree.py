"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
"""


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion answer
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))


class Solution2:
    # bfs answer
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # we use deque for queue data type
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            # the number of iteration is depth of the tree
            for _ in range(len(queue)):
                node = queue.popleft()
                # if the node has childs, push to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
