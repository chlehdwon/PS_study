class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        ans = set()
        lookup = {}
        for i, each in enumerate(nums):
            lookup[each] = i
        print(lookup)
        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j, b in enumerate(nums[i+1:]):
                c = -a-b
                if c in lookup and lookup[c] > j+i+1:
                    ans.add((a, b, c))
        return list(list(s) for s in ans)

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

    def threeSum_3(self, nums):
        nums.sort()
        ans = set()
        if len(nums) <= 2:
            return ans
        for i, num in enumerate(nums[:-2]):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j, target in enumerate(nums[i+1:-1]):
                target_num = -num - target
                if target_num in nums[i+j+2:]:
                    ans.add((num, target, target_num))
        return [list(s) for s in ans]


a = Solution()
print(a.threeSum_3([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
