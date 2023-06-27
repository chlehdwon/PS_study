# Given a non-empty string s and a dictionary wordDict containing
# a list of non-empty words, determine if s can be segmented into
# a space-separated sequence of one or more dictionary words.


# I can't solve this probelm...
# So, I bring 2 leetcode's answers. Both of answers used DP.

class Solution:
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            # any return True when there is true in given parameters.
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]


class Solution2:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
