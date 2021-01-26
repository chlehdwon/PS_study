"""
Given the root node of a binary search tree, return the sum of values
of all nodes with a value in the range [low, high].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # my solution. If node.val is not in the range, then stop searching.
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def recursive(node):
            if node is None:
                return
            if node.val > high:
                recursive(node.left)
                return
            elif node.val < low:
                recursive(node.right)
                return
            num_in_range.append(node.val)
            recursive(node.left)
            recursive(node.right)
            return

        num_in_range = []
        recursive(root)

        return sum(num_in_range)


class Solution2:
    # book answer. it is more simple than my solution.
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def recursive(node):
            if node is None:
                return 0
            if node.val > high:
                return recursive(node.left)
            elif node.val < low:
                return recursive(node.right)
            return node.val + recursive(node.left) + recursive(node.right)

        return recursive(root)


class Solution3:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # DFS iteration using stack
        # We can easily change to BFS solution by using pop(0).
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum
