# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


class Solution:
    dynamic = []

    def recursive_unique(self, m, n):
        if m > n:
            m, n = n, m
        if self.dynamic[m-1][n-1]:
            return self.dynamic[m-1][n-1]
        else:
            if min(n, m) == 1:
                self.dynamic[m-1][n-1] = 1
            elif min(n, m) == 2:
                self.dynamic[m-1][n-1] = max(n, m)
            else:
                for i in range(m):
                    # print(i, m-i-1, "and", m-i-1, n+i-m)
                    self.dynamic[m-1][n-1] += \
                        self.recursive_unique(i+1, m-i) * \
                        self.recursive_unique(m-i, n+i+1-m)
        return self.dynamic[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        self.dynamic = [[0 for i in range(max(m, n))] for j in range(min(m, n))]
        return self.recursive_unique(m, n)


a = Solution()
print(a.uniquePaths(3, 7))
