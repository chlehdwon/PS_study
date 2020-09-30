# Given two integers dividend and divisor, divide two integers
# without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.


class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                print(i, dividend, temp, res)
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


a = Solution()
print(a.divide(50, -4))
