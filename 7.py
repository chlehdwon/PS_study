# Given a 32-bit signed integer, reverse digits of an integer.abs()


class Solution:
    def reverse(self, x):
        max = (1 << 31) - 1
        min = ~(1 << 31) + 1
        if x > 0:
            a = int(str(x)[::-1])
            if a > max:
                return 0
            else:
                return a
        else:
            b = -int(str(-x)[::-1])
            if b < min:
                return 0
            else:
                return b

    def reverse_f(self, x):
        s = -1 if (x < 0) else 1
        num = int(str(abs(x))[::-1])
        if (num > -2147483648 and num < 2147483647):
            return num*s
        else:
            return 0


a = Solution()
print(a.reverse(1534236469))
print(a.reverse(-312))

