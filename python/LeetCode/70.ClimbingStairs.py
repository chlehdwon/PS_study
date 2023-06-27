"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""


import collections


class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation solution
        if n <= 2:
            return n

        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


class Solution2:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        # memoization solution
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        else:
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]


class Solution3:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a


a = Solution()
print(a.climbStairs(5))
