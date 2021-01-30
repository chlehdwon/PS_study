"""
Given the head of a linked list, return the list after sorting it in
ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1)
memory (i.e. constant space)?
"""


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        print(head.val)
        right, slow, fast = None, head, head
        while fast and fast.next:
            right, slow, fast = slow, slow.next, fast.next.next
        right.next = None
        node1 = self.sortList(head)
        node2 = self.sortList(slow)

        return self.merge(node1, node2)


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        # Linked List to Python List
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        # Sort
        lst.sort()

        # Python List to Linked List
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
