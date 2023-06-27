"""
Given a linked list, swap every two adjacent nodes and return its head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = prev = ListNode(0)
        prev.next = head
        while head and head.next:
            prev.next = head.next
            head.next = head.next.next
            prev.next.next = head

            # move nodes for next compare
            head = head.next
            prev = prev.next.next

        return node.next


class Solution3:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
