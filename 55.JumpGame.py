class Solution:
    def canJump(self, nums) -> bool:
        length = len(nums)
        if nums[0] == 0 and length >= 2:
            return False
        last = length-1
        for i in range(length-1)[::-1]:
            if i+nums[i] >= last:
                last = i
        return last == 0


a = Solution()
print(a.canJump([2,0,0]))
