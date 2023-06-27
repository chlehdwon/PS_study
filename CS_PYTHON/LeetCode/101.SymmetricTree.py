# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetricBst(node1, node2):
    if not node1 and not node2:
        return True
    elif not node1 or not node2:
        return False
    else:
        return node1.val == node2.val and \
            isSymmetricBst(node1.left, node2.right) and \
            isSymmetricBst(node1.right, node2.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return isSymmetricBst(root.left, root.right)


a = Solution()
root1 = TreeNode(3, None, None)
root2 = TreeNode(2, left=root1, right=None)
root3 = TreeNode(2, None, root2)
print(a.isSymmetric(root3))
