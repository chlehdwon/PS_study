# 2020-09-08
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

import time


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :my code
        """
        start_time = time.time()
        for i, num in enumerate(nums):
            if target-num in nums[i+1:]:
                j = nums[i+1:].index(target-num)+i+1
                print(f"-----{(time.time() - start_time):.10f}-----")
                return list((i, j))
        return []

    def twoSum_f(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :faster code
        """
        start_time = time.time()
        h = {}
        for i, num in enumerate(nums):
            if target-num in h:
                print(f"-----{(time.time() - start_time):.10f}-----")
                return [h[target-num], i]
            if num not in h:
                h[num] = i
        return []


a = Solution()
print(a.twoSum([1, 2, 2, 4, 10, 5], 7))
print(a.twoSum_f([1, 2, 2, 4, 10, 5], 7))
