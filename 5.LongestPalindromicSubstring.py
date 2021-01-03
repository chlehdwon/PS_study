# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome(self, s):
        def longestPalindromeCenteredAt(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]
        result = ''
        for i in range(len(s)):
            newResult = longestPalindromeCenteredAt(i, i)
            if len(newResult) > len(result):
                result = newResult
            if i + 1 < len(s):
                newResult = longestPalindromeCenteredAt(i, i + 1)
                if len(newResult) > len(result):
                    result = newResult
        return result


class Solution2:
    def longestPalindrome(self, s):
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
