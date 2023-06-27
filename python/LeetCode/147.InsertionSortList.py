"""
Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            cur = parent
        return cur.next


class Solution2:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent

        return parent.next

