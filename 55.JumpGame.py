class Solution:
    def canJump(self, nums) -> bool:
        if nums[0] >= len(nums) - 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(1, nums[0]+1):
            if self.canJump(nums[i:]):
                return True
        return False


a = Solution()
print(a.canJump([3,0,8,2,0,0,1]))
