"""
Given an integer array nums of 2n integers, group these integers into n
pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of
min(ai, bi) for all i is maximized. Return the maximized sum.
"""


class Solution:
    # General solution.
    # We can easily know that the sum of even index number is the maximum.
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(len(nums)//2):
            pair_sum += nums[2*i]
        return pair_sum


class Solution2:
    # solution which is the way of python
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
