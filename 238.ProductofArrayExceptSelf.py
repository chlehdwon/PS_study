"""
Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # left product // [1, a, a*b, a*b*c]
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # right product // [b*c*d, c*d, d, 1]
        # return the product of left and right
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
