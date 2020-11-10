# Given a binary tree, return the zigzag level order traversal of its
# nodes' values. (ie, from left to right, then right to left
# for the next level and alternate between).

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        return_list = []
        flag = 1
        while len(queue) > 0:
            ans = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                ans.append(node.val)
                if flag == 1:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if flag == -1:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
            return_list.append(ans)
            flag *= -1
        return return_list

