# You are climbing a stair case. 
# It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        elif n == 2:
            return 2
        else:
            dynamic = [0 for i in range(n)]
            dynamic[0], dynamic[1] = 1, 2
            for i in range(2, n):
                dynamic[i] = dynamic[i-1] + dynamic[i-2]
            return dynamic[-1]


class Solution2:
    def climbStairs(self, n: int) -> int:
    	a, b = 1, 1
    	for i in range(n): a, b = b, a + b
    	return a


a = Solution()
print(a.climbStairs(5))