# Given head, the head of a linked list, determine
# if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's
# next pointer is connected to. Note that pos is not passed as a
# parameter.

# Return true if there is a cycle in the linked list. Otherwise,
# return false.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # General solution solved by hash table.
    def hasCycle(self, head: ListNode) -> bool:
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            else:
                dictionary[head] = True
            head = head.next


class Solution2:
    # This is two-pointer soluiton.
    # slow and fast pointer will iterate the linked list
    # with different spped. slow is one step, fast is two steps.
    # If there is no cycle, then fast will reach the tail earlier.
    # If there is cycle, then slow and fast will meet each other.
    # Space complexity of this solution is O(1).
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
