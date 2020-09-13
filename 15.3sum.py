class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        if len(nums) <= 2:
            return ans
        print(nums)
        for i, num in enumerate(nums[:-2]):
            for j, target in enumerate(nums[i+1:-1]):
                target_num = -num - target
                if target_num in nums[i+2+j:]:
                    print(num, target, target_num)
                    ans.add((num, target, target_num))
        return [list(s) for s in ans]

    def threeSum_2(self, nums):
        nums.sort()
        ans = set()
        for i, v in enumerate(nums):
            self.twoSum(nums[i+1:], -v, ans)
        return list(list(s) for s in ans)

    def twoSum(self, nums, target, ans):
        d = {}
        for i, v in enumerate(nums):
            if target-v in d:
                ans.add((v, target-v, -target))
            d[v] = i


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
