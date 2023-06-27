"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""


from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        length = len(nums)
        for key, value in counter.items():
            if value > length // 2:
                return key


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        # if a is majority in divided lists, then return
        return [b, a][nums.count(a) > half]


class Solution3:
    def majorityElement(self, nums):
        # one pass solution. If there is a mjority element,
        # count can't be go to the minus when we finally iterate the list.
        count = 0
        curr = ''
        for i in nums:
            if i == curr:
                count += 1
            else:
                if count <= 0:
                    curr = i
                    count = 1
                else:
                    count -= 1

        return curr


class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

