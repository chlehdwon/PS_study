# A linked list is given such that each node contains an additional
# random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# The Linked List is represented in the input/output
# as a list of n nodes. Each node is represented as a pair of
# [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1)
# where random pointer points to,
# or null if it does not point to any node.

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# My answer. But I referenced the hint.
# For example when we want to copy A->B->C->D,
# Then we make A', B', C', D' and connect it like:
# A->A'->B->B'->C->C'->D->D'.
# Then change the connection.
# By this method, we don't need any new space.

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        pointer = head
        while pointer:
            newnode = Node(x=pointer.val, next=pointer.next,
                           random=pointer.random)
            pointer.next = newnode
            pointer = pointer.next.next
        pointer = head.next
        while pointer.next:
            pointer.next = pointer.next.next
            if pointer.random:
                pointer.random = pointer.random.next
            pointer = pointer.next
        if pointer.random:
            pointer.random = pointer.random.next
        return head.next


# Little bit different answer. This anwer used hash-map by dictionary.


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]
