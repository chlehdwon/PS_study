# You are given two non-empty linked lists representing
# two non-negative integers.
# The digits are stored in reverse order and
# each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# # Definition for singly-linked list.async


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()
        n_l1, n_l2, n_l3, carry = l1, l2, l3, 0
        while n_l1 is not None or n_l2 is not None:
            if not n_l1:
                v_l1, v_l2 = 0, n_l2.val
            elif not n_l2:
                v_l1, v_l2 = n_l1.val, 0
            else:
                v_l1, v_l2 = n_l1.val, n_l2.val
            c_val = v_l1 + v_l2 + carry
            if c_val >= 10:
                n_l3.val = c_val - 10
                carry = 1
            else:
                n_l3.val = c_val
                carry = 0
            if n_l1:
                n_l1 = n_l1.next
            if n_l2:
                n_l2 = n_l2.next
            if n_l1 or n_l2:
                n_l3.next = ListNode()
                n_l3 = n_l3.next
        if carry:
            n_l3.next = ListNode(1)
        return l3


a = Solution()
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next, n2.next = n2, n3
n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
n4.next, n5.next = n5, n6
n7 = a.addTwoNumbers(n1, n4)
print(n7.val, n7.next.val, n7.next.next.val, n7.next.next.next.val)
