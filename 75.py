"""
Given an array nums with n objects colored red, white, or blue, sort
them in-place so that objects of the same color are adjacent, with the
colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white,
and blue, respectively.
"""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_0, i, index_1 = 0, 0, len(nums)-1
        while i < index_1:
            if nums[i] == 0:
                nums[i], nums[index_0] = nums[index_0], nums[i]
                index_0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[index_1] = nums[index_1], nums[i]
                index_1 -= 1
            else:
                i += 1
        return nums


a = Solution()
print(a.sortColors([2,0,1]))
