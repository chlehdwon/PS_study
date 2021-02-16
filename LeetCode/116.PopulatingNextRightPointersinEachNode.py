# You are given a perfect binary tree where all leaves are on the same
# level, and every parent has two children. The binary tree has the
# following definition:

# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be
# set to NULL.

# Initially, all next pointers are set to NULL.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# I use 2 list to solve this problem. Because it is easy to hadle
# the last node of the level. First, we check which node list is
# empty. Because we will put the childs of the other node list's node.

# And then we will connect the other node list's node with 'next'.
# In this part, we will pop the nodes to make node_list empty.
# And also, the last popped node's next element will be None.

# We will perform that until the both lists are empty which means
# we reach at the bottom of the tree. Then, return the root.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        node_list1 = [root]
        node_list2 = []
        while True:
            if not node_list2:
                if not node_list1:
                    return root
                else:
                    for node in node_list1:
                        if node.left:
                            node_list2.append(node.left)
                            node_list2.append(node.right)
                    for i in range(len(node_list1)):
                        node = node_list1.pop(0)
                        if node_list1:
                            node.next = node_list1[0]
                        else:
                            node.next = None
            else:
                if not node_list2:
                    return root
                else:
                    for node in node_list2:
                        if node.left:
                            node_list1.append(node.left)
                            node_list1.append(node.right)
                    for i in range(len(node_list2)):
                        node = node_list2.pop(0)
                        if node_list2:
                            node.next = node_list2[0]
                        else:
                            node.next = None


# Actually, we can solve this problem simply by using two keys:
# above and below.

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        above, below = root, root.left
        while below:
            cur = below
            while above:
                if cur == above.left:
                    cur.next = above.right
                    above = above.next
                else:
                    cur.next = above.left
                cur = cur.next

            above = below
            below = below.left

        return root
