"""
Given two strings s and t , write a function to determine
if t is an anagram of s.
"""


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s:
            tracker[x] += 1
        for x in t:
            tracker[x] -= 1
        return all(x == 0 for x in tracker.values())

