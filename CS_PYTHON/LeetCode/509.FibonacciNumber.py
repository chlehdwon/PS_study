"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


import collections


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp = [0 for _ in range(n+1)]
            dp[0], dp[1] = 0, 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


class Solution2:
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        self.dp[1] = 1
        if n <= 1:
            return self.dp[n]
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)

        return self.dp[n]


class Solution3:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x

