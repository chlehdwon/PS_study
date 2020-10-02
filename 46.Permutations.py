# Given a collection of distinct integers,
# return all possible permutations.


class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        output = []
        output_prev = self.permute(nums[:-1])
        last = nums[-1]
        length = len(nums)
        for prev in output_prev:
            for i in range(length):
                a = prev[:]
                a.insert(i, last)
                output.append(a)
        return output


class Solution2:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]
    """

    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subset+[nums[i]], nums)
                visited.remove(i)


a = Solution()
print(a.permute([7]))
print(a.permute([1, 2, 3, 4]))
