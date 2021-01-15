"""
Given a non-empty array of integers, return the k most frequent elements.
"""

import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # insert hip in negative numbers becuase heapq is mean-heap
        # so, we can pop the most frequent one directly
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # pop k times from heapq
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


class Solution2:
    # pythonic way answer
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
