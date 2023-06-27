# A message containing letters from A-Z is being encoded to numbers
# using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits,
# determine the total number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.


class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.helper(s)

    def helper(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s in self.memo:
            return self.memo[s]

        takeOne = takeTwo = 0

        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = self.helper(s[1:])
        if int(s[:2]) >= 10 and int(s[:2]) <= 26:
            takeTwo = self.helper(s[2:])

        self.memo[s] = takeOne + takeTwo

        return self.memo[s]


class Solution2:
    def numDecodings(self, s):
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]


a = Solution()
print(a.numDecodings("230"))
