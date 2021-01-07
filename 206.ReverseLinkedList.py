"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative solution by using prev
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev
            

class Solution2:
    # recursion solution
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)