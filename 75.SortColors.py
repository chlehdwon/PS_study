# Given an array nums with n objects colored red, white, or blue, sort
# them in-place so that objects of the same color are adjacent, with the
# colors in the order red, white, and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red,
# white, and blue respectively.


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        First Solution : Just Sort the array by using selection sort
        """
        for i in range(len(nums)-1):
            minimum = i
            if nums[i] == 0:
                continue
            for j in range(i+1, len(nums)):
                if nums[minimum] > nums[j]:
                    minimum = j
            nums[i], nums[minimum] = nums[minimum], nums[i]


class Solution2:
    def sortColors(self, nums) -> None:
        """
        Second Solution : Count the number of 1, 2 and change array
        """
        count1 = 0
        count2 = 0
        for i in nums:
            if i == 1:
                count1 += 1
            if i == 2:
                count2 += 1
        for i in range(len(nums)-count1-count2):
            nums[i] = 0
        for i in range(len(nums)-count1-count2, len(nums)-count2):
            nums[i] = 1
        for i in range(len(nums)-count2, len(nums)):
            nums[i] = 2


class Solution3:
    def sortColors(self, nums):
        """
        Third Solution : The Dutch national flag problem
        l,m and h satisfy the condition l<=m<=h
        Range 0 to l will be position of '0'
        Range l+1 to m will be position of '1'
        Range m+1 to h will be position of '2'
        """
        h = len(nums)-1
        l, m = 0, 0
        while m <= h:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[h], nums[m] = nums[m], nums[h]
                h = h-1


a = Solution()
a.sortColors([2,0,2,1,1,0])
