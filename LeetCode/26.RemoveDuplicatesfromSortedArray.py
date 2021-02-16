# Given a sorted array nums, remove the duplicates in-place
# such that each element appear only once and return the new length.

# Do not allocate extra space for another array,
# you must do this by modifying the input array
# in-place with O(1) extra memory.


class Solution:
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

    def removeDuplicates_f(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            curr_val = nums[i]
            if nums[i+1] == curr_val:
                nums.pop(i)
            else:
                curr_val = nums[i+1]
                i += 1
        return len(nums)


a = Solution()
print(a.removeDuplicates([1, 1, 2]))
