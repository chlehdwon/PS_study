# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together
# the nodes of the first two lists.
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        n_l3 = l3 = ListNode()
        while l1 or l2:
            if not l1:
                n_l3.next = l2
                break
            elif not l2:
                n_l3.next = l1
                break
            else:
                if l1.val <= l2.val:
                    n_l3.next = l1
                    n_l3 = n_l3.next
                    l1 = l1.next
                elif l1.val > l2.val:
                    n_l3.next = l2
                    n_l3 = n_l3.next
                    l2 = l2.next
        return l3.next


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
            


a = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next, n2.next = n2, n3
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next, n5.next = n5, n6
n7 = a.mergeTwoLists_2(n1, n4)
while n7:
    print(n7.val)
    n7 = n7.next















