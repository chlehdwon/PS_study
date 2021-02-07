"""
Given a string s that consists of only uppercase English letters, you
can perform at most k operations on that string.

In one operation, you can choose any character of the string and change
it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating
letters you can get after performing the above operations.
"""


import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = collections.Counter()
        left, right, count, life = 0, 0, 0, k
        for right, c in enumerate(s):
            a[c] += 1
            if s[left] != c:
                life -= 1
            if life == 0:
                while left < right and s[left] == c:
                    a[c[left]] -= 1
                    left += 1
                if not count or a[c[left]] > count:
                    count = a[c[left]]
                life = k

        return count + k