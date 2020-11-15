# Given preorder and inorder traversal of a tree,
# construct the binary tree.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Leetcode's answer. Basically, we make node by preorder.
    # After find the index of the node in inorder list, we can
    # know that left side of inorder list will be placed in
    # left side of the tree, and right side of list will be placed in
    # right side of the tree. So by using recusion, we can built the
    # tree easily.
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root


class Solution2:
    # Leetcode's answer. This code use helper method to avoid
    # list slicing.
    def buildTree(self, preorder, inorder):
        val_index_dict = {num: idx for idx, num in enumerate(inorder)}
        self.root_index = 0

        def helper(left, right):
            if left > right:
                # Base case:
                # return None as empty Node
                return None
            else:
                # Recall:
                # definition of preorder traversal: Center, Left, Right
                # rebuild with direction of definition
                root = TreeNode(preorder[self.root_index])
                # update root index
                self.root_index += 1
                mid = val_index_dict[root.val]
                root.left = helper(left, mid-1)
                root.right = helper(mid+1, right)
                return root
        # ----------------------------------------------------
        return helper(left=0, right=len(inorder)-1)

