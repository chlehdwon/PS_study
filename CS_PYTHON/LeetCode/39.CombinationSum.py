"""
Given an array of distinct integers candidates and a target integer
target, return a list of all unique combinations of candidateswhere the
chosen numbers sum to target. You may return the combinations in any
order.

The same number may be chosen from candidates an unlimited number of
times. Two combinations are unique if the frequency of at least one of
the chosen numbers is different.
abs()
It is guaranteed that the number of unique combinations that sum up to
target is less than 150 combinations for the given input.
"""


class Solution:
    def combinationSum(self, candidates, target: int):
        def backtracking(elements, target):
            # finish condition
            if target == 0:
                answer.append(elements[:])
                return
            # case for when the target is less than minimum elements
            min_ele = elements[0] if elements else 0
            if target < min_ele:
                return
            start = can_dict[elements[-1]] if elements else 0
            # call recursively after append elements after start
            for num in candidates[start:]:
                elements.append(num)
                backtracking(elements, target-num)
                elements.pop()
        # it is easy when we have sorted list
        candidates = sorted(candidates)
        answer = []
        # dictionary which stores elements: its index for candidates
        can_dict = {candidates[i]: i for i in range(len(candidates))}
        backtracking([], target)
        return answer


class Solution2:
    def combinationSum(self, candidates, target: int):
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


class Solution3:
    # fastest dp solution
    def combinationSum(self, denoms, targetSum: int):
        dp = [[] for _ in range(targetSum + 1)]
        dp[0] = [[]]

        for denom in denoms:  # for each new coin
            for amount in range(1, targetSum + 1):
                if denom <= amount:
                    for coinCombination in dp[amount - denom]:
                        dp[amount].append(coinCombination + [denom])

        return dp[-1]  # just return the last element at index == target sum


a = Solution()
print(a.combinationSum([2,7,6,3,5,1], 9))

