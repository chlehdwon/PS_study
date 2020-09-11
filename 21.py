# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        n_l1, n_l2, n_l3, num = l1, l2, None, 0
        if n_l1.val >= nl2.val:
            n_l3 = n_l2
            num = 1
        else:
            n_l3 = n_l1
            num = 0
        while (not n_l1) and (not n_l2):
            if num == 0:
                if n_l1.next.val < n_l2.val:
                    n_l3.next = n_l1.next
                    n_l1.next = n_l1
                else:
                    n_13.next = n_l2
                    n_l2.next = n_l2
                    num = 1
            else:
                if n_l2.next.val < n_l1.val:
                    n_l3.next = n_l2.next
                    n_l2.next = n_l2
                    num = 0
                else:
                    n_13.next = n_l1
                    n_l1.next = n_l1
        return l3