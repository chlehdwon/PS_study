"""
Calculate the sum of two integers a and b, but you are not allowed to
use the operator + and -.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # Implement full adder
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        if carry == 1:
            result.append('1')

        # when result exceeds the limit
        result = int(''.join(result[::-1]), 2) & MASK
        # negative case
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result


class Solution2:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        # sum and carry
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # negative case
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a
