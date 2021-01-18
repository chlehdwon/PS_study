"""
Given two integers n and k, return all possible combinations of k
numbers out of 1 ... n.

You may return the answer in any order.
"""

import itertools


class Solution:
    def combine(self, n: int, k: int):
        def dfs(comb):
            # append elements with k-length to result
            if len(comb) == k:
                result.append(comb[:])
                return
            # recursion with after elements
            for i in range(comb[-1], n):
                comb.append(i+1)
                dfs(comb)
                comb.pop()

        result = []
        for i in range(n-k+1):
            dfs([i+1])
        return result


class Solution2:
    # book answer. different version of dfs
    def combine(self, n: int, k: int):
        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        results = []
        dfs([], 1, k)
        return results


class Solution3:
    def combine(self, n: int, k: int):
        return list(itertools.combinations(range(1, n+1), k))


a = Solution()
print(a.combine(4, 2))
