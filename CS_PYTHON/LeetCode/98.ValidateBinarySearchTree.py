# Given a binary tree, determine if it is a valid binary search tree

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than
# the node's key.
# The right subtree of a node contains only nodes with keys greater
# than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorderTraversal(root)
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True

    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + \
            [root.val] + self.inorderTraversal(root.right)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right:
                    return False
                return rec(node.left, left, node.val) and \
                    rec(node.right, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf'))


a = Solution()
root1 = TreeNode(1, None, None)
root2 = TreeNode(3, None, None)
root3 = TreeNode(3, root1, root2)
print(a.isValidBST(root3))
