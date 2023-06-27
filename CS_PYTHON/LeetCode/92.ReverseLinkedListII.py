"""
Reverse a linked list from position m to n. Do it in one-pass.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or m == n:
            return head
        # because we need to get prev node of start point of reversing
        rev_prev = ListNode(0)
        rev_prev.next = rev_head = head
        # find the start point of reversing
        for _ in range(m-1):
            rev_prev = rev_prev.next
        rev_head = rev_prev.next
        # which means m is the length of list
        if rev_head.next is None:
            return head
        else:
            rev_node = rev_head
            rev_next = rev_head.next
        # reverse each node
        for _ in range(n-m):
            temp = rev_next.next
            rev_next.next = rev_node
            rev_node = rev_next
            rev_next = temp
        rev_head.next = rev_next
        rev_prev.next = rev_node
        # special case because if m is 1, rev_prev is prev of head
        if m == 1:
            return rev_prev.next
        return head


class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # for exception case
        if head is None or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root.next
