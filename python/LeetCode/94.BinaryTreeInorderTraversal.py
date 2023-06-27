# Given the root of a binary tree,
# return the inorder traversal of its nodes' values.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + \
            [root.val] + self.inorderTraversal(root.right)


class Solution2:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


a = Solution2()
root1 = TreeNode(3, None, None)
root2 = TreeNode(2, left=root1, right=None)
root3 = TreeNode(1, None, root2)
print(a.inorderTraversal(root3))
