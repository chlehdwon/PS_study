"""
You are given an array of k linked-lists lists, each linked-list is
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # save each listnode's head in the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        # after doing pop from heap, save next node in the heap.
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
