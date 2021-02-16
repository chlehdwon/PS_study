"""
You are given an integer array nums sorted in ascending order
(with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum value and set it to pivot
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        left, right = 0, len(nums) - 1

        # binary search by using center as pivot
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] > target:
                right = mid - 1
            elif nums[mid_pivot] < target:
                left = mid + 1
            else:
                return mid_pivot
        return -1


class Solution2:
    def search(self, nums, target: int) -> int:
        check = True
        if nums[0] > target:
            check = False
            if nums[-1] < target:
                return -1
        for i, num in enumerate(nums):
            if target == num:
                return i
            if check:
                if target < num:
                    return -1
            if target > num:
                check = True
        return -1


class Solution3:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif start == mid and mid == end:
                return -1
            elif nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target < nums[start]:
                    start = mid + 1
                else:
                    end = mid
        return -1


a = Solution()
print(a.search([4, 5, 6, 7, 0, 1, 2], 0))
