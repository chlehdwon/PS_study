# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left, right = -1, length-1
        for i in range(length-1):
            if nums[i]<nums[i+1]:
                left = i
        if left>=0:
            while nums[left]>=nums[right]:
                right-=1
            nums[left],nums[right]=nums[right],nums[left]
        self.reverse(left+1,nums)
    
    def reverse(self, i, nums):
        j = len(nums)-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1