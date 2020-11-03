# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).abs()

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        def inorderTraversal(self, root):
            if not root:
                return []
            return self.inorderTraversal(root.left) + \
                [root.val] + self.inorderTraversal(root.right)
        left_inorder = self.inorderTraversal(root.left)
        right_inorder = self.inorderTraversal(root.right)
        return left_inorder[::-1] == right_inorder


a = Solution()
root1 = TreeNode(3, None, None)
root2 = TreeNode(2, left=root1, right=None)
root3 = TreeNode(1, None, root2)
print(a.isSymmetric(root3))
