# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
from typing import List

class Solution:
    cache = []

    # top-down answer
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.cache = [[[-1]*n] for _ in range(m)]
        
        return self.dp(0, 0, grid)

    # bottom-up answer
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j>0:
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                elif j==0 and i>0:
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                elif i>0 and j>0:
                    grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
        
        return grid[-1][-1]
    
    def dp(self, y: int, x: int, grid: List[List[int]]) -> int:
        print(self.cache, y, x)
        if self.cache[y][x] != -1:
            return self.cache[y][x]
        else:
            m, n = len(grid), len(grid[0])
            if y==m-1 and x==n-1:
                self.cache[-1][-1] = grid[-1][-1]
                return self.cache[-1][-1]
            elif y==m-1:
                self.cache[y][x] = grid[y][x] + self.dp(y,x+1,grid)
                return self.cache[y][x]
            elif x==n-1:
                self.cache[y][x] = grid[y][x] + self.dp(y+1,x,grid)
                return self.cache[y][x]
            else:
                self.cache[y][x] = grid[y][x] + min(self.dp(y+1,x,grid), self.dp(y,x+1,grid))
                return self.cache[y][x]

a = Solution()
print(a.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))