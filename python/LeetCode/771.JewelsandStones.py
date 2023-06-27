"""
You're given strings jewels representing the types of stones that are
jewels, and stones representing the stones you have. Each character in
stones is a type of stone you have. You want to know how many of the
stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of
stone from "A".
"""


import collections


class Solution:
    # my answer by usign defaultdict
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.defaultdict(int)
        num = 0
        for s in stones:
            counter[s] += 1
        for j in jewels:
            num += counter[j]
        return num


class Solution2:
    # more simple way by using Counter
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        num = 0
        for j in jewels:
            num += counter[j]
        return num


class Solution3:
    # pythonic way which uses list comprehension and sum()
    # the answer is sum of [s in jewels for s in stones]
    # ex) [True, False, True, True] for jewels = "aA" and stones = "abAA"
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

