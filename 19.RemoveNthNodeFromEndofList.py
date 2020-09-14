# Definition for singly-linked list.
# Given a linked list, remove the n-th node
# from the end of list and return its head.ArithmeticError


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        node = head
        while node:
            check = node
            for i in range(n+1):
                if i == n and not check:
                    return head.next
                check = check.next
            if not check:
                node.next = node.next.next
                break
            else:
                node = node.next
        return head

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        if not head or not n:
            return head
        ans = []
        while(head):
            ans.append(head)
            head = head.next
        if len(ans) == 1:
            return head
        if n == 1:
            ans[-n-1].next = None
            return ans[0]
        if len(ans) == n:
            return ans[1]
        ans[-n-1].next = ans[-n+1]
        return ans[0]


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
a = Solution()
n6 = a.removeNthFromEnd(n1, 5)
n7 = a.removeNthFromEnd_2(n1, 5)
while n7:
    print(n7.val)
    n7 = n7.next

