# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be 
# a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated
# and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2 if x > 5 else x
        if x == 0 or x == 1:
            return x
        else:
            while True:
                mid = (low + high) // 2
                if mid ** 2 == x:
                    return mid
                elif mid ** 2 < x:
                    low = mid
                else:
                    high = mid
                if (low + high) // 2 == mid:
                    return mid

a = Solution()
print(a.mySqrt(5))