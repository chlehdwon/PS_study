# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never
# differ by more than 1.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST((nums[mid+1:]))

        return root

    def sortedArrayToBST_2(self, nums):
        def traverse(l, r):
            if l > r:
                return
            m = (r + l)//2
            node = TreeNode(nums[m])
            node.left = traverse(l, m - 1)
            node.right = traverse(m + 1, r)
            return node
        return traverse(0, len(nums) - 1)
