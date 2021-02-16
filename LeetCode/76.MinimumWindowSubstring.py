"""
Given two strings s and t, return the minimum window in s which will
contain all the characters in t. If there is no such window in s that
covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will
always be only one unique minimum window in s.
"""


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # move right pointer
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # if missing char is 0, then validate whether we have to move the left pointer
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            # Validate whether we have to move the left pointer by using AND operation between counters
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        return s[start: end] if end - start <= len(s) else ''


a = Solution()
print(a.minWindow(s = "ADOBECODEBANC", t = "ABC"))
