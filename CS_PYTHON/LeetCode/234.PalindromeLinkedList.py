import collections
"""
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # make reverse linked list by using runner
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # case for when the length of list is odd.
            if fast:
                slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        return val_list == val_list[::-1]


class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        val_list = collections.deque()
        while head is not None:
            val_list.append(head.val)
            head = head.next
        while len(val_list) > 1:
            if val_list.popleft() != val_list.pop():
                return False
        return True