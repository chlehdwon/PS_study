# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).


class Solution:
    def searchRange(self, nums, target: int):
        start, end = 0, len(nums)-1
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if start == end:
                if nums[mid] == target:
                    return [mid, mid]
                else:
                    return [-1, -1]
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                first, last = mid, mid
                while first > start and first > 0:
                    first -= 1
                    if nums[first] != target:
                        first += 1
                        break
                while last < end and last < len(nums)-1:
                    last += 1
                    if nums[last] != target:
                        last -= 1
                        break
                return [first, last]
        return [-1, -1]


class Solution2:
    def searchRange(self, nums, target: int):
        def binarysearch(flag):
            ans = -1
            le = 0
            r = len(nums) - 1
            while le <= r:
                mid = (le + r) // 2
                if nums[mid] == target:
                    if flag == "LEFT":
                        ans = mid
                        r = mid - 1
                        continue
                    else:
                        ans = mid
                        le = mid + 1
                        continue
                if nums[mid] < target:
                    le = mid + 1
                else:
                    r = mid - 1
            return ans
        left = binarysearch("LEFT")
        right = binarysearch("RIGHT")
        return [left, right]


a = Solution()
print(a.searchRange([2, 2, 2, 2, 2], 2))
print(a.searchRange([5, 7, 7, 8, 8, 10], 6))
