"""
Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
"""

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
