"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary
tree in which the depth of the two subtrees of every node never differ
by more than 1.
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # My answer. I used recursion to solve this problem.
    # To make height-balanced bst, I used half-point of index
    # for the root.
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        # Divide and Conquer
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


class Solution2:
    # More updated version
    # Because time is wasted when we slice the 'nums' list
    # So, by using the traverse function which have two parameters
    # l and r. These parameters allow us to avoid the slicing.
    def sortedArrayToBST(self, nums):
        def traverse(l, r):
            if l > r:
                return
            m = (r + l)//2
            node = TreeNode(nums[m])
            node.left = traverse(l, m - 1)
            node.right = traverse(m + 1, r)
            return node
        return traverse(0, len(nums) - 1)
