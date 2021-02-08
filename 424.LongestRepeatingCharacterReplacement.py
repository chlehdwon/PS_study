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
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # search the number of the most common character
            max_char_n = counts.most_common(1)[0][1]

            # move left pointer if the value exceeds k
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
