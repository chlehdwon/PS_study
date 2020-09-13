# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        def findpoint(head, n):
            while n > 0:
                head = head.next
                n -= 1
            if head:
                return True
            else:
                return False
        prev, node = ListNode(0, head), head
        while node:
            if findpoint(node, n):
                prev.next = head.next
                break
            head, prev = head.next, head
        return head
