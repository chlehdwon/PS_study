"""
You are given an array of integers nums, there is a sliding window of
size k which is moving from the very left of the array to the very
right. You can only see the k numbers in the window. Each time the
sliding window moves right by one position.

Return the max sliding window.
"""


import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = collections.deque(), []
        for i in range(len(nums)):
            if i-k >= 0:
                res.append(nums[q[0]])
                while q and q[0] <= i - k:
                    q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res

