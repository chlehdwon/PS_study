"""
The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1
            xor = xor >> 1
        return count


