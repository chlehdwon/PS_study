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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n_l3 = l3 = ListNode(0)
        carry, sum = 0, 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                sum = (carry + l2.val) % 10
                carry = (carry + l2.val) // 10
            elif l2 is None:
                sum = (carry + l1.val) % 10
                carry = (carry + l1.val) // 10
            else:
                sum = (carry + l1.val + l2.val) % 10
                carry = (carry + l1.val + l2.val) // 10
            n_l3.val = sum
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 or l2 or carry:
                n_l3.next = ListNode(1)
                n_l3 = n_l3.next
        return l3


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # plus each node's value to sum
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # calculate carry and remainder by uising divmod()
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


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
