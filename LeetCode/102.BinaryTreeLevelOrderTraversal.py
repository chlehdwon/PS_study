# Given a binary tree, return the level order traversal of its nodes'
# values. (ie, from left to right, level by level).

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        value_list = []
        node_list = [root]
        while True:
            temp1, temp2 = [], []
            for node in node_list:
                if node.left:
                    temp1.append(node.left.val)
                    temp2.append(node.left)
                if node.right:
                    temp1.append(node.right.val)
                    temp2.append(node.right)
            if temp2:
                value_list.append(temp1)
                node_list = temp2
            else:
                break
        return value_list


class Solution2:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        return_list = []
        while len(queue) > 0:
            ans = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list

