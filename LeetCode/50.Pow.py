# Implement pow(x, n), which calculates x raised to the power n
# (i.e. x^n).


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x**n == (1/x)**(-n)
        if n < 0:
            x = 1/x
            n = -n
        # We solve the positive power here:
        power = 1
        current_product = x
        while n > 0:
            # if n is odd numberm, we need to time x one more time
            if n % 2:
                power = power * current_product
            current_product = current_product * current_product
            n = n//2
        return power


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            if n % 2 == 1:
                return x * tmp * tmp

        if n >= 0:
            return helper(x, n)

        return 1 / helper(x, -n)


a = Solution()
print(a.myPow(2.1, 3))
print(a.myPow(2, -2))
