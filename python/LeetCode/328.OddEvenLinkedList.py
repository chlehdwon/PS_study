"""
Given a singly linked list, group all odd nodes together followed
by the even nodes. Please note here we are talking about
the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = next = head.next
        while odd and odd.next:
            odd.next = odd.next.next
            if odd.next:
                even.next = even.next.next
                even = even.next
                odd = odd.next
        odd.next = next
        return head


class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = next = head.next
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = next
        return head

