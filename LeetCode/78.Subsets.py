"""
Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the
solution in any order.
"""


class Solution:
    def subsets(self, nums):
        def dfs(index, ele):
            ans.append(ele[:])
            for i in range(index+1, len(nums)):
                ele.append(nums[i])
                dfs(i, ele)
                ele.pop()
        ans = []
        dfs(-1, [])
        return ans


class Solution2:
    def subsets(self, nums):
        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        result = []
        dfs(0, [])
        return result


class Solution3:
    def subsets(self, nums):
        if not nums:
            return []
        length = len(nums)
        result = []
        for i in range(2**(length-1)):
            elements_1 = []
            elements_2 = []
            for j in range(length):
                if i & 2**j:
                    elements_1.append(nums[j])
                else:
                    elements_2.append(nums[j])
            result.append(elements_1)
            result.append(elements_2)
        return result


class Solution4:
    """
    level 0: []
    level 1: [11]                    [22]       [33]
    level 2: [11,22]     [11,33]     [22,33]
    level 3: [11,22,33]
    """

    def subsets(self, nums):
        res = []
        self.backtracking(res, 0, [], nums)
        return res

    def backtracking(self, res, start, subset, nums):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtracking(res, i+1, subset, nums)
            subset.pop()


a = Solution2()
print(a.subsets([1, 2, 3]))
