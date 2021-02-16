"""
Write a function that takes an unsigned integer and returns the number
of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages such as Java, there is no unsigned integer
type. In this case, the input will be given as a signed integer type.
It should not affect your implementation, as the integer's internal
binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's
complement notation.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (1 & n)
            n = n >> 1
        return count


class Solution2:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class Solution3:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
