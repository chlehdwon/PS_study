# # Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum

# # Follow up: If you have figured out the O(n) solution, try coding
# another solution using the divide and conquer approach, which is more
# subtle.


class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        ##############################################################
        # Kadane's Algorithm   O(n)

        current_sum = float('-inf')
        max_sum = 0
        for i in range(n):
            current_sum = max(current_sum+nums[i], nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum

        ###############################################################
        # divide and Conquer O(nlogn)

        if n == 1:
            return nums[0]

        m = n//2

        left_sum = self.maxSubArray(nums[:m])
        right_sum = self.maxSubArray(nums[m:])

        max_left_sum = float("-inf")
        max_right_sum = float("-inf")

        sum_ = 0
        for i in range(m-1, -1, -1):
            sum_ += nums[i]
            max_left_sum = max(max_left_sum, sum_)

        sum_ = 0
        for i in range(m, n):
            sum_ += nums[i]
            max_right_sum = max(max_right_sum, sum_)

        return max(left_sum, right_sum, max_left_sum+max_right_sum)


a = Solution()
print([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
