# You are given an integer array nums sorted in ascending order,
# and an integer target.


class Solution:
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


class Solution2:
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
